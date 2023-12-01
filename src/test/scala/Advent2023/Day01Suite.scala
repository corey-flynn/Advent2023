package Advent2023

import org.scalatest.funsuite.AnyFunSuite

class Day01Suite extends AnyFunSuite:
  val example: String =
    """1abc2
      |pqr3stu8vwx
      |a1b2c3d4e5f
      |treb7uchet""".stripMargin

  val example_two: String =
    """two1nine
      |eightwothree
      |abcone2threexyz
      |xtwone3four
      |4nineeightseven2
      |zoneight234
      |7pqrstsixteen""".stripMargin

  test("Part 1 should be the same as the example solution.") {
    assert(Day01.part1(example) == 142)  // Place real example solution here
  }

  test("Part 2 should be the same as the example solution.") {
    assert(Day01.part2(example_two) == 281)  // Place real example solution here
  }