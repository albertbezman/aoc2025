from __future__ import annotations

import sys
from dataclasses import dataclass, field


def parse_file() -> tuple[ProductRange, ...]:
    data = sys.stdin.read().rstrip("\n")
    ranges = data.split(",")

    all_ranges = []
    for r in ranges:
        start, end = r.split("-") 
        pr = ProductRange(int(start), int(end))
        all_ranges.append(pr)

    return tuple(all_ranges)

def iter_and_sum_ranges(ranges: tuple[ProductRange, ...], ir: IterRanges) -> int:
    for r in ranges:
        for num in range(r.start, r.end + 1):
            if is_num_repeated_twice(num):
                ir.invalid_ids.append(num)
    return ir.summed_invalid_ids



def is_num_repeated_twice(num: int) -> bool:
    str_num = str(num)
    len_num = len(str_num)
    if len_num % 2 == 0:
        len_half = int(len_num / 2)
        left = str_num[:len_half]
        right = str_num[len_half:]
        if left == right:
            return True

    return False

@dataclass
class ProductRange:
    start: int
    end: int

    def __post_init__(self):
        if self.start > self.end:
            raise ValueError

@dataclass
class IterRanges:
    invalid_ids: list[int] = field(default_factory=list)
    
    @property
    def summed_invalid_ids(self) -> int:
        return sum(self.invalid_ids)

def main() -> None:
    prs = parse_file()
    ir = IterRanges()
    summed_ids = iter_and_sum_ranges(prs, ir)
    print(summed_ids)


if __name__ == "__main__":
    main()
