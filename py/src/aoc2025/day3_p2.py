from __future__ import annotations

import sys
from dataclasses import dataclass, field

NUM_BATS = 12


def parse_file() -> tuple[Bank, ...]:
    data = sys.stdin.read().rstrip("\n")
    banks = data.split("\n")
    all_banks = [Bank(value=b) for b in banks]
    return tuple(all_banks)


def find_max_num_in_sequence(seq_str: str) -> tuple[int, int]:
    nums = [int(n) for n in seq_str]
    # TODO: doing max and .index redundant, can reduce to O(n) from O(2n)
    max_num = max(nums)
    max_idx = nums.index(max_num)
    return max_num, max_idx


def process_banks(banks: tuple[Bank, ...]) -> int:
    total = 0
    for bank in banks:
        left_idx = 0
        val = bank.value
        for i in range(NUM_BATS - 1, 0 - 1, -1):
            if i != 0:
                val_slice = val[left_idx:-i]
            else:
                val_slice = val[left_idx:]
            max_num, max_idx = find_max_num_in_sequence(val_slice)
            left_idx += max_idx + 1
            bank.max_battery_array.append(max_num)
        total += bank.max_joltage
    return total


@dataclass
class Bank:
    value: str
    max_battery_array: list[int] = field(default_factory=list)

    @property
    def max_joltage(self):
        if len(self.max_battery_array) != NUM_BATS:
            raise Exception
        return int("".join(str(x) for x in self.max_battery_array))


def main() -> None:
    banks = parse_file()
    total_joltage = process_banks(banks)
    print(total_joltage)


if __name__ == "__main__":
    main()
