#!/bin/bash

# build
cargo build --bin day1

# run
cargo run --bin day1

# test
cargo test --bin day1

# format
cargo fmt
cargo fmt -- --check
