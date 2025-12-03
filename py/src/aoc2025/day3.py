from __future__ import annotations

import sys
from dataclasses import dataclass


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
        val = bank.value
        left_max_num, left_max_idx = find_max_num_in_sequence(val[:-1])
        right_max_num, _ = find_max_num_in_sequence(val[left_max_idx + 1 :])
        bank.left_max = left_max_num
        bank.right_max = right_max_num
        total += bank.max_joltage
    return total


@dataclass
class Bank:
    value: str
    left_max: int | None = None
    right_max: int | None = None

    @property
    def max_joltage(self):
        if self.left_max is None or self.right_max is None:
            raise Exception
        return int(f"{self.left_max}{self.right_max}")


def main() -> None:
    banks = parse_file()
    total_joltage = process_banks(banks)
    print(total_joltage)


if __name__ == "__main__":
    main()
