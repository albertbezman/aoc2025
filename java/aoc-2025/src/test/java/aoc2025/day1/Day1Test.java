package aoc2025.day1;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Day01Test {

    @Test
    void examplePart1() {
        // Arrange
        String input = "sample input here";

        // Act
        int result = Day1.solvePart1(input);

        // Assert
        assertEquals(42, result);   // replace with expected value
    }

    @Test
    void examplePart2() {
        String input = "sample input here";

        int result = Day1.solvePart2(input);

        assertEquals(84, result);
    }
}
