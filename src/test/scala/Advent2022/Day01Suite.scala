package Advent2022

import org.scalatest.funsuite.AnyFunSuite

class Day01Suite extends AnyFunSuite:
  val example: String = """
      |1000
      |2000
      |3000
      |
      |4000
      |
      |5000
      |6000
      |
      |7000
      |8000
      |9000
      |
      |10000
    """.stripMargin.trim

  test("Part 1 asserts to the example problem solution of 24,000") {
    assert(Day01.part1(example) == 24_000)
  }

  test("Part 2 asserts to the example problem solution of 45,000") {
    assert(Day01.part2(example) == 45_000)
  }
