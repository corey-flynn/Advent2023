package Advent2023

import org.scalatest.funsuite.AnyFunSuite

class Day03Suite extends AnyFunSuite:
  val example: String =
    """467..114..
      |...*......
      |..35..633.
      |......#...
      |617*......
      |.....+.58.
      |..592.....
      |......755.
      |...$.*....
      |.664.598..""".stripMargin.trim

  test("Part 1 should be the same as the example solution.") {
    assert(Day03.part1(example) == 4_361)
  }

  test("Part 2 should be the same as the example solution.") {
    assert(Day03.part2(example) == 467_835)  // Place real example solution here
  }
