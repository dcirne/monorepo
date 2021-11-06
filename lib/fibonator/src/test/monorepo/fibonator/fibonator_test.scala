package test.monorepo.fibonator

import monorepo.fibonator.Fibonator
import org.scalatest.BeforeAndAfter
import org.scalatest.FunSuite

class FibonatorTest extends FunSuite with BeforeAndAfter {
    var fibonator: Fibonator = _

    before {
        fibonator = new Fibonator()
    }

    test("6th Fibonacci") {
        asset(fibonator.compute_fibonacci(6) == 8)
    }
}
