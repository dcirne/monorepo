import monorepo.fibonator.Fibonator

object Fibonacci {
    def main(args: Array[String]): Unit = {
        val fibonator = new Fibonator()
        val n:Int = 13 
        val f: Int = fibonator.compute_fibonacci(n)
        println(s"The $n th Fibonacci is: $f")
    }
}
