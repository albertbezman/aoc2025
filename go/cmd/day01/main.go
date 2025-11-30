package main

import (
	"log"
	"os"

	"aoc2025/go/internal/aoc2025"
)

func main() {
	if err := aoc2025.RunDay01(os.Stdin, os.Stdout); err != nil {
		log.Fatalf("error: %v", err)
	}
}
