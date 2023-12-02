/*
https://adventofcode.com/2023/day/2
--- Day 2: Cube Conundrum ---
*/

package Advent2023

import scala.util.matching.Regex
import utilities.Timing

object Day02 {

  val gamePattern: Regex = "Game (\\d+): ".r
  val cubePattern: Regex = "(\\d+) (blue|green|red)".r

  private def gameMap(line: String): collection.mutable.Map[String, Int] =
    val ms = collection.mutable.Map("index" -> 0, "blue" -> 0, "green" -> 0, "red" -> 0)
    ms("index") = gamePattern.findFirstMatchIn(line) match { case Some(m) => m.group(1).toInt }

    for (cubes <- cubePattern.findAllMatchIn(line)) {
      if (ms(cubes.group(2)) < cubes.group(1).toInt) {
        ms(cubes.group(2)) = cubes.group(1).toInt
      }
    }
    ms

  private def parse(input: String): Array[Map[String, Int]] =
    val games = input.split("\n")
    for (game <- games) yield gameMap(game).toMap

  def part1(input: String): Int = {
    parse(input).foldLeft(0) { (sum, game) =>
      if (
          game("blue") <= 14 &&
          game("green") <= 13 &&
          game("red") <= 12
      ) { sum + game("index") }
      else sum
    }
  }

  def part2(input: String): Int = {
    parse(input).foldLeft(0) { (power, game) =>
      power + (game("blue") * game("green") * game("red"))
    }
  }

  def main(args: Array[String]): Unit = {
    val data: String = {
      io.Source.fromResource("Advent2023/Day02.txt").mkString
    }
    println(Timing.timing(part1(data)))  // 2331  // 0.056447208 s
    println(Timing.timing(part2(data)))  // 71585 // 0.00635764 s
  }
}