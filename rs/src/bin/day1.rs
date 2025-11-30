fn part1(input: &str) -> i64 {
    // your logic here
    0
}

fn part2(input: &str) -> i64 {
    // your logic here
    0
}

fn main() {
    let input = include_str!("../../../inputs/day01.txt");
    println!("{}", part1(input));
    println!("{}", part2(input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_part1() {
        let input = "\
example line 1
example line 2
";
        assert_eq!(42, part1(input));
    }

    #[test]
    fn example_part2() {
        let input = "\
example line 1
example line 2
";
        assert_eq!(123, part2(input));
    }
}
