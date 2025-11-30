#!/bin/bash

# compile
mvn -q compile

# run
java -cp target/classes aoc2025.day1.Day1
