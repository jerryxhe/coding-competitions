/* https://www.hackerrank.com/challenges/super-digit */

object Solution {

    def super_digit(n:String): Int = {
        if(n.length ==1) (n.toInt-0)
        else {
          super_digit(n.toList.map(_.toInt-48).sum.toString())
        }
    }
    
    def main(args: Array[String]) {
        val row  = scala.io.StdIn.readLine().split(' ')
        val base = row.head
        val times = row.tail.head.toLong
        println(super_digit((super_digit(base)*times).toString))
    }
}
