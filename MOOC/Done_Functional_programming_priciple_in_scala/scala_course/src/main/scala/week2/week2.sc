import scala.annotation.tailrec



/*================ 2.1 ================*/
def factorial(n: Int): Int = {
  if (n == 0) return 1
  else return n * factorial(n-1)
}
@tailrec
def trail_rec_factorial(n: Int, acc: Int): Int={
  if (n==0) return acc
  else return trail_rec_factorial(n-1, acc * n)
}
trail_rec_factorial(10, 1)
factorial(10)


/*============ 2.2 =========================*/
/*sum with high order functions*/
def sum(f: Int => Int, a: Int, b: Int): Int={
  if (a>b) 0
  else f(a) + sum(f, a+1, b)



def id(x: Int): Int = x
def cube(x: Int): Int = x*x*x

def sumInts(a: Int, b:Int): Int= sum(id, a, b)
def sumCubes(a: Int, b: Int): Int = sum(cube, a, b)

sumInts(1, 3)
sumCubes(1, 3)

/*improve with anonymous functions*/

def sumInts2(a: Int, b: Int): Int = sum(x => x, a, b)
def sumCubes2(a: Int, b: Int): Int = sum(x => x*x*x, a, b)

sumInts2(1, 3)
sumCubes2(1, 3)


/*Exercise*/
// can't tell the meaning of questions
def fact(x: Int): Int = {
  if (x==0) 1
  else x * fact(x -1)
}
def sumFactorial(a:Int, b:Int): Int = sum(fact, a, b)

sumFactorial(1, 3)

/*==========2.3 =============*/



//def sum(f: Int => Int): (Int, Int) => Int = {
//  def sumF(a: Int, b: Int): Int ={
//    if (a > b) 0
//    else f(a) + sumF(a+1, b)
//  }
//  sumF
//}

  def sum(f: Int => Int)(a: Int, b: Int):  Int = {
    def sumF(a: Int, b: Int): Int ={
      if (a > b) 0
      else f(a) + sumF(a+1, b)
    }
    sumF(a, b)
  }
//sum(cube)(1, 3)

def tail_rec_sum(f: Int => Int)(a: Int, b: Int): Int={
  def loop(a: Int, acc: Int): Int= {
    if (a > b) acc
    else loop(a+1, acc + f(a))
  }
  loop(a, 0)
}


sum(cube)(1, 3)
tail_rec_sum(cube)(1, 3)

sum(id)(2, 300)
tail_rec_sum(id)(2, 300)

//def sumInts = sum(x => x)
//
//sumInts(1, 2)

//sum(id)(1, 2)

//sum(cube)(1, 2)

/*exercise*/

//def sum(f: Int => Int)(a: Int, b: Int): Int={
//  def loop(a: Int, acc: Int): Int= {
//
//  }
//  loop()
//}


/*=========== 2.4 ===============*/


val tolerance = 0.0001
//def isCloseEnough(x: Double, y: Double) =
//  Math.abs((x - y) / x) / x < tolerance
//
//def fixedPoint(f: Double => Double)(firstGuess: Double) = {
//  def iterate(guess: Double): Double = {
//    val next = f(guess)
//    println(next)
//    if (isCloseEnough(guess, next)) next
//    else iterate(next)
//  }
//  iterate(firstGuess)
//}
//def averageDamp(f:Double => Double)(x: Double) = (x + f(x)) / 2
//
//// original version
//def sqrt(x: Double) = fixedPoint(y => x/y)(1.0)
//
//sqrt(2)
//
////  + averageDamping
//def sqrt(x:Double): Double = fixedPoint(averageDamp(y => x/y))(1)
//


