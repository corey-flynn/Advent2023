/*
https://adventofcode.com/2023/day/1
--- Day 1: Trebuchet?! ---
*/

package Advent2023

import utilities.Timing

object Day01 {

  private val spelledDigits: Map[String, String] = Map(
    "one" -> "1",
    "two" -> "2",
    "three" -> "3",
    "four" -> "4",
    "five" -> "5",
    "six" -> "6",
    "seven" -> "7",
    "eight" -> "8",
    "nine" -> "9",
  )

  private def findInString(s: String, values: Array[String]): Int = {
    // find the first and last values in a string, transform them to ints, and return
    val occurrences = values.flatMap { value =>
      s.indices
        .filter(idx => s.startsWith(value, idx))
        .map(idx => (idx, value))
    }.sortBy(_._1)
    val firstVal = spelledDigits.getOrElse(occurrences.head._2, occurrences.head._2)
    val lastValue = spelledDigits.getOrElse(occurrences.last._2, occurrences.last._2)
    (firstVal + lastValue).toInt
  }

  private def parse(s: String, values: Array[String]): Seq[Int] = {
    val lines: Array[String] = s.split("\n")
    lines.map(line => findInString(line, values))
  }

  def part1(input: String): Int = {
    val searchValues = spelledDigits.values.toArray
    parse(input, searchValues).sum
  }

  def part2(input: String): Int = {
    // use both keys and values from the spelledDigits Map
    val searchValues = spelledDigits.flatMap {
      case (key, value) => Seq(key, value)
    }.toArray
    parse(input, searchValues).sum
  }

  def main(args: Array[String]): Unit = {
    val data: String = {
      io.Source.fromResource("Advent2023/Day01.txt").mkString
    }
    println(Timing.timing(part1(data)))  // 56506 // 0.05367502 s
    println(Timing.timing(part2(data)))  // 56017 // 0.015446345 s
  }
}