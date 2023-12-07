/*
https://adventofcode.com/2023/day/3
*/

package Advent2023

import scala.util.matching.Regex
import scala.collection.mutable

import utilities.Timing

object Day03 {
  private def adjParts(a: Int, b: Int): Seq[(Int, Int)] = {
    for {
      a_ <- Seq(a - 1, a, a + 1)
      b_ <- Seq(b - 1, b, b + 1)
    } yield (a_, b_)
  }

  def parse(input: String, gears: Boolean = false): Int = {
    val numPattern: Regex = "\\d+".r
    val lines = input.split("\n")
    val symbolSet = lines.zipWithIndex.flatMap {
      case (line, j) => line.zipWithIndex.collect {
        case (char, i) if !char.isDigit && char != '.' => (i, j)
      }
    }.toSet
    val gearMap = mutable.Map[(Int, Int), mutable.ListBuffer[Int]]()
    val partNumSum = mutable.ListBuffer[Int]()

    lines.zipWithIndex.foreach { case (line, j) =>
      numPattern.findAllMatchIn(line).foreach { nums =>
        val n = nums.matched.toInt
        val intersectionFound = (nums.start until nums.end).exists { i =>
          val intersection = adjParts(i, j).toSet.intersect(symbolSet)
          intersection.nonEmpty && {
            intersection.foreach { case sym@(x, y) =>
              if (lines(y)(x) == '*') {
                if (gearMap.contains(sym)) gearMap(sym) += n else gearMap(sym) = mutable.ListBuffer(n)
              }
            }
            true
          }
        }
        if (intersectionFound && !gears) {
          partNumSum += n
        }
      }
    }
    if (gears) {
      gearMap.values.collect { case v if v.length == 2 => v.product }.sum
    }
    else partNumSum.sum
  }

  def part1(input: String): Int =
    parse(input)

  def part2(input: String): Int =
    parse(input, gears = true)

  def main(args: Array[String]): Unit =
    val data: String = io.Source.fromResource("Advent2023/Day03.txt").mkString
    part1(data)
    println(Timing.timing(part1(data)))  // 528799   // 0.024264736 s
    println(Timing.timing(part2(data)))  // 84907174 // 0.028974002 s
}
