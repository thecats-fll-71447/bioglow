"""Load Cat-Bot's program onto a hub, after you pick which hub.

Run it from VS Code: Ctrl+Shift+P -> Tasks: Run Task -> Load program onto robot
Or from the terminal (with the .venv turned on):

    python tools/load_robot.py          load it; start it with the center button
    python tools/load_robot.py --run    load it and start it now (shows print output)

What it does:
  1. Looks for every Pybricks hub that is turned on nearby (5 seconds).
  2. Lists them, closest first, and asks you to type the number of YOUR hub.
  3. Loads robot/main.py (and every run file) onto that hub only.

Nothing is loaded until you type a number, so code never goes to the
wrong robot by accident.
"""

import argparse
import asyncio
import subprocess
import sys
from collections import Counter
from pathlib import Path

from bleak import BleakScanner
from pybricksdev.ble.pybricks import PYBRICKS_SERVICE_UUID

SCAN_SECONDS = 5
PROGRAM = Path(__file__).resolve().parent.parent / "robot" / "main.py"


def signal_words(rssi):
    """Turn Bluetooth signal strength into words. Closer hubs are stronger."""
    if rssi is None:
        return "unknown"
    if rssi >= -60:
        return "strong (very close)"
    if rssi >= -75:
        return "medium"
    return "weak (far away)"


async def find_hubs():
    """Return a list of (name, address, rssi) for every Pybricks hub nearby."""
    found = await BleakScanner.discover(timeout=SCAN_SECONDS, return_adv=True)
    hubs = []
    for device, adv in found.values():
        if PYBRICKS_SERVICE_UUID not in adv.service_uuids:
            continue  # some other Bluetooth thing: a phone, headphones...
        name = adv.local_name or device.name or "(no name)"
        hubs.append((name, device.address, adv.rssi))
    hubs.sort(key=lambda hub: hub[2] if hub[2] is not None else -999, reverse=True)
    return hubs


def choose_hub(hubs):
    """Show the hubs and ask which one. Returns one hub, or None to cancel."""
    name_counts = Counter(name for name, _, _ in hubs)
    print()
    print(f"Found {len(hubs)} Pybricks hub(s):")
    for number, (name, address, rssi) in enumerate(hubs, start=1):
        print(f"  {number}) {name:<18} signal: {signal_words(rssi)}")
        if name_counts[name] > 1:
            print(f"     ^ more than one hub is named {name!r}. Use signal")
            print("       strength to tell them apart, or rename one.")
    print()
    while True:
        answer = input("Type the number of YOUR hub, then Enter (just Enter = cancel): ").strip()
        if answer == "":
            return None
        if answer.isdigit() and 1 <= int(answer) <= len(hubs):
            return hubs[int(answer) - 1]
        print(f"  Please type a number from 1 to {len(hubs)}.")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--run", action="store_true",
                        help="start the program right away and show its output")
    args = parser.parse_args()

    print(f"Looking for hubs that are turned on ({SCAN_SECONDS} seconds)...")
    hubs = asyncio.run(find_hubs())
    if not hubs:
        print()
        print("No hubs found. Check that:")
        print("  - the hub is turned on (if a program is running on it, stop it),")
        print("  - this computer's Bluetooth is on,")
        print("  - the hub isn't still connected to Pybricks Code or another laptop")
        print("    (a connected hub stays hidden).")
        return 1

    hub = choose_hub(hubs)
    if hub is None:
        print("Cancelled. Nothing was loaded.")
        return 0
    name, address, _ = hub

    print(f"Loading onto {name}...")
    command = [sys.executable, "-m", "pybricksdev", "run", "ble",
               "--name", address]  # the address picks exactly this hub
    if not args.run:
        command.append("--no-start")
    command.append(str(PROGRAM))
    result = subprocess.call(command)
    if result == 0 and not args.run:
        print(f"Done. The program is on {name}. Start it with the center button.")
    return result


if __name__ == "__main__":
    sys.exit(main())
