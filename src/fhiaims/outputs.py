# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from typing import Any, TextIO


def parse_aims(f: TextIO) -> Any:
    line = next(l for l in f if "Total energy uncorrected" in l)
    results = {"total_energy": float(line.split()[5])}
    return results
