
object execise {
  println("hello world")
}

// recursion
def factorial(n: Int): Int={
  if (n == 0) 1 else n*factorial(n-1)
}

factorial(0)

factorial(4)

// tail recursion
def tailFatorial(n: Int): Int ={
  def loop(acc: Int, n: Int): Int = {
    if (n == 0) acc
    else loop(acc*n, n-1)
  }
  loop(1, n)
}
tailFatorial(1)
tailFatorial(4)


