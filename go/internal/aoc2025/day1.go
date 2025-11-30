package aoc2025

import (
	"bufio"
	"fmt"
	"io"
)

func Day01Part1(input string) int {
	// TODO: implement
	return 0
}

func Day01Part2(input string) int {
	// TODO: implement
	return 0
}

func RunDay01(r io.Reader, w io.Writer) error {
	scanner := bufio.NewScanner(r)
	var data string
	for scanner.Scan() {
		if data != "" {
			data += "\n"
		}
		data += scanner.Text()
	}
	if err := scanner.Err(); err != nil {
		return err
	}

	fmt.Fprintf(w, "Part 1: %d\n", Day01Part1(data))
	fmt.Fprintf(w, "Part 2: %d\n", Day01Part2(data))
	return nil
}
