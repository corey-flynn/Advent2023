package utilities

object Timing {
  def timing[A](f: => A): A = {
    val startTime = System.nanoTime()
    val result = f
    val endTime = System.nanoTime()
    val duration = (endTime - startTime) / 1e9
    println(s"Execution took: $duration s")
    result
  }
}
