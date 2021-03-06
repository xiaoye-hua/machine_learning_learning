package stackoverflow

import org.scalatest.{FunSuite, BeforeAndAfterAll}
import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.rdd.RDD
import java.io.File

@RunWith(classOf[JUnitRunner])
class StackOverflowSuite extends FunSuite with BeforeAndAfterAll {
  val config: SparkConf = new SparkConf().setMaster("local").setAppName("test")
  val sc: SparkContext = new SparkContext(config)

  lazy val testObject = new StackOverflow {
    override val langs =
      List(
        "JavaScript", "Java", "PHP", "Python", "C#", "C++", "Ruby", "CSS",
        "Objective-C", "Perl", "Scala", "Haskell", "MATLAB", "Clojure", "Groovy")
    override def langSpread = 50000
    override def kmeansKernels = 45
    override def kmeansEta: Double = 20.0D
    override def kmeansMaxIterations = 120
  }

  test("testObject can be instantiated") {
    val instantiatable = try {
      testObject
      true
    } catch {
      case _: Throwable => false
    }
    assert(instantiatable, "Can't instantiate a StackOverflow object")
  }

  test("groupedPostings test"){
//    import stackoverflow.
    val postList = List(
      Posting(1, 1, Some(1), None, 10, Some("Java"))
      , Posting(1, 2, Some(1), None, 10, Some("Java"))
      , Posting(1, 6, Some(1), None, 10, Some("Java"))
      , Posting(2, 3, Some(1), Some(1), 10, Some("Java"))
      , Posting(2, 4, Some(1), Some(1), 10, Some("Java"))
      , Posting(2, 5, Some(1), Some(2), 10, Some("Java"))
    )
    val postRDD = sc.parallelize(postList)
    val result = testObject.groupedPostings(postRDD)
//    println()
//    println(result.collect())
    assert(result.collect().length === 2, "groupedPosting failed")
  }

  test("scoredPostings"){
    val groupedPostingsList = Array(
      (1, Iterable(
        (Posting(1, 1, Some(1), None, 10, Some("Java")), Posting(2, 3, Some(1), Some(1), 40, Some("Java")))
        , (Posting(1, 1, Some(1), None, 10, Some("Java")), Posting(2, 4, Some(1), Some(1), 0, Some("Java")))
      ))
      , (2, Iterable(
        (Posting(1, 2, Some(1), None, 10, Some("Java")), Posting(2, 5, Some(1), Some(2), 30, Some("Java")))
      ))
    )
    val groupedPostingRDD = sc.parallelize(groupedPostingsList)
    val result = testObject.scoredPostings(groupedPostingRDD)
    val target = Set(
      (Posting(1, 1, Some(1), None, 10, Some("Java")), 40)
      , (Posting(1, 2, Some(1), None, 10, Some("Java")), 30)
    )
    assert(result.collect().toSet === target)
  }

  test("VectorPosting"){
    import StackOverflow.{langSpread, langs}
    val scoredRDD = sc.parallelize(
      List(
        (Posting(1, 1, Some(1), None, 10, Some("Java")), 40)
        , (Posting(1, 2, Some(1), None, 10, Some("PHP")), 30)
      )
    )
    val target = Set(
      (50000, 40),
      (100000, 30)
    )
    val result = testObject.vectorPostings(scoredRDD)
    assert(result.collect().toSet === target)

  }

  val a = Array(
    (1, "q")
    , (1, "w")
    , (1, "y")
    , (2, "h")
    , (3, "h")
    , (5, "h")
  )

}
