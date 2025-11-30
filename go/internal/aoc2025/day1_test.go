package aoc2025

import "testing"

func TestDay1Part1(t *testing.T) {
    got := Part1("example input")
    want := 42

    if got != want {
        t.Fatalf("Part1() = %d, want %d", got, want)
    }
}

func TestDay1Part2(t *testing.T) {
    got := Part2("more example")
    want := 99

    if got != want {
        t.Fatalf("Part2() = %d, want %d", got, want)
    }
}
