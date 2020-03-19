"""High level Verifiable Delay Function using keccak (sha3)."""
from hashlib import sha3_256
from typing import Union
import time
from statistics import mean
from math import ceil

from .mimc import forward_mimc, reverse_mimc
"""
Kevin Froman 2020

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
DEFAULT_ROUNDS = 8000


def _sha3_256_hash(data: bytes) -> str:
    sha3 = sha3_256()
    sha3.update(data)
    return sha3.hexdigest()


def vdf_create(data: bytes, rounds: int = DEFAULT_ROUNDS) -> str:
    assert rounds > 1
    input_hash = int(_sha3_256_hash(data), 16)
    return hex(forward_mimc(input_hash, rounds)).replace('0x', '')


def vdf_verify(
        data: bytes,
        test_hash: Union[str, bytes],
        rounds: int = DEFAULT_ROUNDS) -> bool:
    """Verify data for test_hash generated by vdf_create."""
    assert rounds > 1
    return _sha3_256_hash(data) == \
        hex(reverse_mimc(int(test_hash, 16), rounds)).replace('0x', '')


def profile_cpu_speed(seconds=1) -> float:
    n = 2
    start = time.time()
    done = False
    results = []
    try:
        for _ in range(20):
            done = False
            n = 2
            start = time.time()
            while not done:
                vdf_create(b't', n)
                if time.time() - start >= seconds:
                    break
                n += 1
            results.append(n)
    except KeyboardInterrupt:
        pass
    return ceil(mean(results))


if __name__ == "__main__":
    print("Calculate how may rounds are needed for X seconds (influenced by system processes): ")
    seconds = int(input("Seconds: "))
    print("Rounds:", profile_cpu_speed(seconds))
