package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
      if ((c == r) || (c == 0)) 1
      else pascal(c-1, r-1) + pascal(c, r-1)
    }
  
  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {
      def loop(chars: List[Char], cnt: Int): Boolean ={
        println(chars)
        println(cnt)
        if (chars.isEmpty) return cnt == 0
        if (cnt < 0) return false
        if (chars.head == '(') {
          return loop(chars.tail, cnt + 1)
        }
        if (chars.head == ')') {
          return loop(chars.tail, cnt - 1)
        }
        return loop(chars.tail, cnt)
      }
      loop(chars, 0)
    }
  
  /**
   * Exercise 3
   */
    def countChange(money: Int, coins: List[Int]): Int = {
      if (money == 0) return 1
      if (money < 0) return 0
      if (coins.length <=0 & money >=1) return 0
      return countChange(money, coins.tail) + countChange(money-coins.head, coins)

    }
  }
