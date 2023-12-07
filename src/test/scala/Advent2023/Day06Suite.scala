package Advent2023

import org.scalatest.funsuite.AnyFunSuite

class Day06Suite extends AnyFunSuite:
  val example: String =
    """Time:      7  15   30
      |Distance:  9  40  200""".stripMargin.trim

  test("Part 1 should be the same as the example solution.") {
    assert(Day06.part1(example) == 288)
  }

  test("Part 2 should be the same as the example solution.") {
    assert(Day06.part2(example) == 71_503)
  }
