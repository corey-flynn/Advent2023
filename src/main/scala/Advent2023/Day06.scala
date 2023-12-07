/*
https://adventofcode.com/2023/day/6
*/

package Advent2023

import utilities.Timing

import scala.collection.mutable.ArrayBuffer

object Day06 {

  private def parse(input: String): Array[Array[Long]] =
    val Array(times, distance) = input.split("\n")
    val timesArray: Array[Long] = times.split("\\s+").drop(1).map(_.toLong)
    val distanceArray: Array[Long] = distance.split("\\s+").drop(1).map(_.toLong)
    Array(timesArray, distanceArray)

  private def mostWins(time: Long, record: Long): Long =
    var minTime: Long = 0
    var maxTime: Long = time
    while (minTime * (time - minTime) <= record) {
      minTime += 1
    }
    while ((time - maxTime) * maxTime <= record) {
      maxTime -= 1
    }
    1 + maxTime - minTime

  def part1(input: String): Long = {
    val raceArray: ArrayBuffer[Long] = ArrayBuffer()
    val parsedInput = parse(input)
    for (race <- parsedInput(0) zip parsedInput(1)) {
      raceArray += mostWins(race(0), race(1))
    }
    raceArray.product
  }

  def part2(input: String): Long = {
    val Array(timesArray, distanceArray) = parse(input)
    val time: Long = timesArray.map(_.toString).mkString.toLong
    val distance: Long = distanceArray.map(_.toString).mkString.toLong
    mostWins(time, distance)
  }

  def main(args: Array[String]): Unit = {
    val data: String = {
      io.Source.fromResource("Advent2023/Day06.txt").mkString
    }
    part1(data)
    println(Timing.timing(part1(data)))  // 625_968    // 0.000223396 s
    println(Timing.timing(part2(data)))  // 43_663_323 // 0.009269027 s
  }
}
