package monorepo.fibonator

class Fibonator() {
    def compute_fibonacci(n : Int): Int = { 
        def recurse_fibonacci(n: Int, a: Int, b: Int): Int = n match {
            case 0 => a 
            case _ => recurse_fibonacci(n - 1, b, a + b)
        }
        
        return recurse_fibonacci(n, 0, 1)
    }
}
