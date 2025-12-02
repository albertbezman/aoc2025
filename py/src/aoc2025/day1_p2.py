from __future__ import annotations

import sys
from dataclasses import dataclass


def parse_file() -> RotationInstructions:
    data = sys.stdin.read().rstrip("\n")
    rotations = data.split("\n")

    all_instructions = []
    for r in rotations:
        op = r[:1]
        num = r[1:]
        i = Instruction(op, int(num))
        all_instructions.append(i)

    return RotationInstructions(sequence=tuple(all_instructions))


def iter_instructions(ris: RotationInstructions, rs: RotationState) -> int:
    for instruction in ris.sequence:
        if instruction.operation == "L":
            rs.decr(instruction.integer)
        elif instruction.operation == "R":
            rs.incr(instruction.integer)
        else:
            raise Exception("op not supported")
    return rs.final_zero_count


@dataclass
class Instruction:
    operation: str
    integer: int


@dataclass
class RotationInstructions:
    sequence: tuple[Instruction, ...]


@dataclass
class RotationState:
    current_val: int = 50
    hit_zero_count: int = 0
    crossed_zero_count: int = 0
    modulo_val: int = 100

    def incr(self, x: int) -> None:
        s = self.current_val
        m = self.modulo_val

        a = m if s == 0 else m - s

        if a > x:
            n_hits = 0
        else:
            n_hits = 1 + (x - a) // m

        new_val = (s + x) % m

        if new_val == 0 and n_hits > 0:
            self.hit_zero_count += 1
            self.crossed_zero_count += n_hits - 1
        else:
            self.crossed_zero_count += n_hits

        self.current_val = new_val

    def decr(self, x: int) -> None:
        s = self.current_val
        m = self.modulo_val

        a = m if s == 0 else s

        if a > x:
            n_hits = 0
        else:
            n_hits = 1 + (x - a) // m

        new_val = (s - x) % m

        if new_val == 0 and n_hits > 0:
            self.hit_zero_count += 1
            self.crossed_zero_count += n_hits - 1
        else:
            self.crossed_zero_count += n_hits

        self.current_val = new_val

    @property
    def final_zero_count(self) -> int:
        return self.hit_zero_count + self.crossed_zero_count


def main() -> None:
    ris = parse_file()
    rs = RotationState()
    zero_count = iter_instructions(ris, rs)
    print(zero_count)


if __name__ == "__main__":
    main()
