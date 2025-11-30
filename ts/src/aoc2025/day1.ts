export function part1(input: string): number {
  return 0;
}

export function part2(input: string): number {
  return 0;
}

export function main() {
  const fs = require('fs');
  const input = fs.readFileSync(0, 'utf8').trim(); // stdin
  console.log('Part 1:', part1(input));
  console.log('Part 2:', part2(input));
}

if (require.main === module) {
  console.log('asdf');
  main();
}
