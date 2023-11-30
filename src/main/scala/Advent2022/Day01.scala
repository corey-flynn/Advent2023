package Advent2022

object Day01 {
  private def parse_string(input: String): Seq[Int] = {
    input.split("\n\n").map(_.split("\n").map(_.toInt).sum).toSeq
  }

  def part1(input: String): Int = {
    parse_string(input).max
  }

  def part2(input: String): Int = {
    parse_string(input).sorted.takeRight(3).sum
  }

  def main(args: Array[String]): Unit = {
    val data: String = {
      io.Source.fromResource("Advent2022/day_01.txt").mkString
    }
    println(part1(data))
    println(part2(data))
  }
}
