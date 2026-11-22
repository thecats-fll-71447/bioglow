"""
check.py -- test the robot code on a laptop, WITHOUT the robot.

    python tests/check.py

What it does
  1. Pretends to be the Pybricks hub (fake motors, fake sensors, fake menu).
  2. Picks menu selections the way you would in a match.
  3. Records every command the code sends to the motors.
  4. Checks for typos/crashes in every run file.
  5. Compares the result to the competition code in archive/ (until you
     intentionally change a run -- then that run will show as CHANGED,
     which is fine as long as you meant to change it).

It can't tell you if the robot will hit the mission model -- only the
table can do that. But it catches typos before you walk to the table.
"""

import builtins
import contextlib
import io
import os
import runpy
import sys
import types

sys.dont_write_bytecode = True  # never use stale cached copies of the robot files

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROBOT_DIR = os.path.join(ROOT, "robot")
BASELINE = os.path.join(ROOT, "archive", "team-2026-11-18", "MissionMenu.py")
SEEDS_BASELINE = os.path.join(ROOT, "archive", "team-2026-11-18", "Mission2_v1_0.py")

TRACE = []
MENU_SCRIPT = []          # list of (selection, attachment_color)
STATE = {"color": None}


# ----------------------------------------------------------------- fakes
class _Const:
    def __init__(self, prefix):
        self._p = prefix

    def __getattr__(self, name):
        return f"{self._p}.{name}"


def _rec(who, what, *a, **k):
    TRACE.append((who, what, a, tuple(sorted(k.items()))))


class _Light:
    def on(self, *a, **k): _rec("hub.light", "on", *a, **k)
    def blink(self, *a, **k): _rec("hub.light", "blink", *a, **k)
    def off(self, *a, **k): _rec("hub.light", "off", *a, **k)


class _IMU:
    def reset_heading(self, *a, **k): _rec("hub.imu", "reset_heading", *a, **k)
    def heading(self): return 0


class PrimeHub:
    def __init__(self, *a, **k):
        self.light = _Light()
        self.imu = _IMU()


class _Control:
    def __init__(self, name):
        self.name = name

    def limits(self, *a, **k):
        if not a and not k:
            return (1000, 2000, 200)
        _rec(self.name + ".control", "limits", *a, **k)


class Motor:
    def __init__(self, port, direction=None, *a, **k):
        self.name = f"Motor({port})"
        self.control = _Control(self.name)

    def __getattr__(self, method):
        def f(*a, **k):
            _rec(self.name, method, *a, **k)
            return 100 if method == "load" else None
        return f


class ColorSensor:
    def __init__(self, port):
        pass

    def color(self):
        return STATE["color"]


class _Dummy:
    def __init__(self, *a, **k): pass
    def __getattr__(self, n): return lambda *a, **k: 0


class DriveBase:
    def __init__(self, *a, **k):
        pass

    def settings(self, *a, **k):
        if not a and not k:
            return (300, 1000, 200, 800)
        _rec("driveBase", "settings", *a, **k)

    def __getattr__(self, method):
        return lambda *a, **k: _rec("driveBase", method, *a, **k)


class StopWatch(_Dummy):
    pass


class _MenuEnd(Exception):
    pass


def hub_menu(*options):
    _rec("menu", "shown", *options)
    if not MENU_SCRIPT:
        return "Q"
    selection, color = MENU_SCRIPT.pop(0)
    if selection not in options:
        raise AssertionError(f"selection {selection!r} is not on the menu {options}")
    STATE["color"] = color
    return selection


def wait(ms):
    _rec("tools", "wait", ms)


def install_fakes():
    builtins.const = lambda x: x
    pb = types.ModuleType("pybricks")
    mods = {
        "hubs": {"PrimeHub": PrimeHub},
        "pupdevices": {"Motor": Motor, "ColorSensor": ColorSensor,
                       "UltrasonicSensor": _Dummy, "ForceSensor": _Dummy},
        "parameters": {n: _Const(n) for n in
                       ["Button", "Color", "Direction", "Port", "Side", "Stop"]},
        "robotics": {"DriveBase": DriveBase},
        "tools": {"wait": wait, "StopWatch": StopWatch, "hub_menu": hub_menu},
    }
    sys.modules["pybricks"] = pb
    for name, attrs in mods.items():
        m = types.ModuleType("pybricks." + name)
        m.__dict__.update(attrs)
        sys.modules["pybricks." + name] = m
        setattr(pb, name, m)


# --------------------------------------------------------------- runner
def run_program(path, script):
    """Run a program with a list of (selection, color) choices; return the trace."""
    for name in list(sys.modules):
        if name == "robot" or name == "main" or name.startswith("run_"):
            del sys.modules[name]
    TRACE.clear()
    MENU_SCRIPT[:] = list(script)
    STATE["color"] = None
    folder = os.path.dirname(path)
    sys.path.insert(0, folder)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            runpy.run_path(path, run_name="__main__")
    finally:
        sys.path.remove(folder)
    return list(TRACE)


FULL_MATCH = [("A", None), ("B", None), ("C", None), ("1", None),
              ("2", "Color.RED"), ("2", "Color.BLUE"), ("2", "Color.YELLOW"),
              ("2", "Color.GREEN")]

SCENARIOS = {
    "full match (A,B,C,1, then 2 with RED,BLUE,YELLOW,GREEN)": FULL_MATCH,
    "only A": [("A", None)],
    "start at 2 (GREEN), then jump back to B": [("2", "Color.GREEN"), ("B", None)],
    "selection 2 with no attachment color": [("2", None)],
}


def run_seeds_compare():
    """run_seeds.run() vs the original Mission2_v1_0.py program."""
    for name in list(sys.modules):
        if name == "robot" or name.startswith("run_"):
            del sys.modules[name]
    sys.path.insert(0, ROBOT_DIR)
    try:
        import run_seeds
        TRACE.clear()
        run_seeds.run()
        new = list(TRACE)
    finally:
        sys.path.remove(ROBOT_DIR)
    if not os.path.exists(SEEDS_BASELINE):
        return new, None
    old = run_program(SEEDS_BASELINE, [])
    # the original program turns the gyro on itself; the menu does that for us
    old = [t for t in old if t[:2] != ("driveBase", "use_gyro")]
    return new, old


def main():
    install_fakes()
    ok = True

    # 1) every file imports without typos
    print("Checking each robot file loads...")
    sys.path.insert(0, ROBOT_DIR)
    for fn in sorted(os.listdir(ROBOT_DIR)):
        if fn.endswith(".py") and fn != "main.py":
            try:
                for name in list(sys.modules):
                    if name == "robot" or name.startswith("run_"):
                        del sys.modules[name]
                __import__(fn[:-3])
                print(f"  OK      {fn}")
            except Exception as e:  # noqa: BLE001
                ok = False
                print(f"  ERROR   {fn}: {type(e).__name__}: {e}")
    sys.path.remove(ROBOT_DIR)

    # 2) menu scenarios: new code vs the competition code
    print("\nComparing main.py to the competition code (archive/)...")
    for label, script in SCENARIOS.items():
        try:
            new = run_program(os.path.join(ROBOT_DIR, "main.py"), script)
        except Exception as e:  # noqa: BLE001
            ok = False
            print(f"  ERROR   {label}: {type(e).__name__}: {e}")
            continue
        if not os.path.exists(BASELINE):
            print(f"  RAN     {label}: {len(new)} commands (no baseline file to compare)")
            continue
        old = run_program(BASELINE, script)
        if new == old:
            print(f"  SAME    {label}: {len(new)} commands, identical to competition code")
        else:
            i = next((i for i, (a, b) in enumerate(zip(new, old)) if a != b), min(len(new), len(old)))
            print(f"  CHANGED {label}: first difference at command #{i + 1}")
            print(f"            competition: {old[i] if i < len(old) else '(ended)'}")
            print(f"            now:         {new[i] if i < len(new) else '(ended)'}")

    print("\nChecking run_seeds.py (not on the menu yet) against Mission2_v1_0.py...")
    try:
        new, old = run_seeds_compare()
        if old is None:
            print(f"  RAN     run_seeds: {len(new)} commands")
        elif new == old:
            print(f"  SAME    run_seeds: {len(new)} commands, identical to Mission2_v1_0.py")
        else:
            print("  CHANGED run_seeds: differs from Mission2_v1_0.py")
    except Exception as e:  # noqa: BLE001
        ok = False
        print(f"  ERROR   run_seeds: {type(e).__name__}: {e}")

    print("\nAll files load." if ok else "\nFix the ERROR lines above.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
