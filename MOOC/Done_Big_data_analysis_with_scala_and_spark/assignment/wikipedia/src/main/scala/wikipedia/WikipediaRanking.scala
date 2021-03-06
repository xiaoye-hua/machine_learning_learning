package wikipedia

import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

import org.apache.spark.rdd.RDD

case class WikipediaArticle(title: String, text: String) {
  /**
    * @return Whether the text of this article mentions `lang` or not
    * @param lang Language to look for (e.g. "Scala")
    */
  def mentionsLanguage(lang: String): Boolean = text.split(' ').contains(lang)
}

object WikipediaRanking {

  val langs = List(
    "JavaScript", "Java", "PHP", "Python", "C#", "C++", "Ruby", "CSS",
    "Objective-C", "Perl", "Scala", "Haskell", "MATLAB", "Clojure", "Groovy")


  val conf: SparkConf = new SparkConf().setAppName("wikipedia").setMaster("local[*]")
  val sc: SparkContext = new SparkContext(conf)
  sc.setLogLevel("WARN")
  // Hint: use a combination of `sc.textFile`, `WikipediaData.filePath` and `WikipediaData.parse`
  val wikiRdd: RDD[WikipediaArticle] = sc.textFile(WikipediaData.filePath).map(l => WikipediaData.parse(l)).cache()
//  val conf: SparkConf = new SparkConf().setAppName("wikipedia").setMaster("local[*]")
//  val sc: SparkContext = new SparkContext(
//    conf
//  )
//  // Hint: use a combination of `sc.textFile`, `WikipediaData.filePath` and `WikipediaData.parse`
////  println(WikipediaData.filePath)
//  val wikiRdd: RDD[WikipediaArticle] = sc.textFile(
////"./src/main/resources/wikipedia/wikipedia.dat"
////  "./src/main/resources/wikipedia/wikipedia.dat"
//    WikipediaData.filePath
//).map{
//    line => WikipediaData.parse(line)
//  }

//  val conf: SparkConf = new SparkConf().setAppName("wikipedia").setMaster("local[*]")
//  val sc: SparkContext = new SparkContext(conf)
  sc.setLogLevel("WARN")
  // Hint: use a combination of `sc.textFile`, `WikipediaData.filePath` and `WikipediaData.parse`
//  val wikiRdd: RDD[WikipediaArticle] = sc.textFile(WikipediaData.filePath).map(l => WikipediaData.parse(l)).cache()

  //  println(wikiRdd.take(3))

  /** Returns the number of articles on which the language `lang` occurs.
   *  Hint1: consider using method `aggregate` on RDD[T].
   *  Hint2: consider using method `mentionsLanguage` on `WikipediaArticle`
   */
//  def isFound(lang:String, article: WikipediaArticle): Int = {
//    if (article.mentionsLanguage(lang)) 1 else 0
//  }
  def occurrencesOfLang(lang: String, rdd: RDD[WikipediaArticle]): Int = {
    rdd.aggregate(0)((sum, article) => sum + (if (article.mentionsLanguage(lang)) 1 else 0), _+_)
  }

//  def occurrencesOfLang(lang: String, rdd: RDD[WikipediaArticle]): Int = {
//    val count = rdd.map{
//      e => if (e.mentionsLanguage(lang)) 1 else 0
//    }
//      .reduce{
//        (x,y) => x + y
//      }
//    count
//  }

  /* (1) Use `occurrencesOfLang` to compute the ranking of the languages
   *     (`val langs`) by determining the number of Wikipedia articles that
   *     mention each language at least once. Don't forget to sort the
   *     languages by their occurrence, in decreasing order!
   *
   *   Note: this operation is long-running. It can potentially run for
   *   several seconds.
   */
  def rankLangs(langs: List[String], rdd: RDD[WikipediaArticle]): List[(String, Int)] = {
    val result = langs.map{
      e => (e, occurrencesOfLang(e, rdd))
    }
    result.sortBy(_._2).reverse
//    result.sortBy(_._2)(Ordering.Int.reverse)
  }
//
  /* Compute an inverted index of the set of articles, mapping each language
   * to the Wikipedia pages in which it occurs.
   */
  def makeIndex(langs: List[String], rdd: RDD[WikipediaArticle]): RDD[(String, Iterable[WikipediaArticle])] = {
    val list = rdd.flatMap{
      e =>
        for (lang <- langs if e.mentionsLanguage(lang)) yield (lang, e)
    }
    list.groupByKey()
  }
  /* (2) Compute the language ranking again, but now using the inverted index. Can you notice
   *     a performance improvement?
   *
   *   Note: this operation is long-running. It can potentially run for
   *   several seconds.
   */
  def rankLangsUsingIndex(index: RDD[(String, Iterable[WikipediaArticle])]): List[(String, Int)] = {
//    val count = for {(lang,lst) <- index} yield (lang, lst.size)
    val ranks = for( (lang, list) <- index ) yield (lang, list.size)
    ranks.collect().toList.sortBy(_._2).reverse
  }
  /* (3) Use `reduceByKey` so that the computation of the index and the ranking are combined.
   *     Can you notice an improvement in performance compared to measuring *both* the computation of the index
   *     and the computation of the ranking? If so, can you think of a reason?
   *
   *   Note: this operation is long-running. It can potentially run for
   *   several seconds.
   */
  def rankLangsReduceByKey(langs: List[String], rdd: RDD[WikipediaArticle]): List[(String, Int)] = {
    val ranks = rdd.flatMap{
      article =>
        for (lang <- langs if article.mentionsLanguage(lang)) yield (lang, 1)
    }.reduceByKey(_+_).collect().toList
    ranks.sortBy(_._2).reverse
  }
//  {
//    rdd.map{
//      e =>
//        var target_langs = List()
//        for (lang <- langs){
//          if (e.mentionsLanguage(lang)){
//            target_langs = lang :: target_langs
//          }
//        }
//        (1, target_langs)
//    }
//    List(("hh", 2))
//      .flatMap{
//        e => e
//      }
//      .map{
//        e => (e._2, e._1)
//      }
//  }
  def main(args: Array[String]) {

    println(wikiRdd.take(3))

    /* Languages ranked according to (1) */
    val langsRanked: List[(String, Int)] = timed("Part 1: naive ranking", rankLangs(langs, wikiRdd))

//    val langsRanked: List[(String, Int)] = timed("Part 1: naive ranking", rankLangs(langs, wikiRdd))


      /* An inverted index mapping languages to wikipedia pages on which they appear */
    def index: RDD[(String, Iterable[WikipediaArticle])] = makeIndex(langs, wikiRdd)

    /* Languages ranked according to (2), using the inverted index */
    val langsRanked2: List[(String, Int)] = timed("Part 2: ranking using inverted index", rankLangsUsingIndex(index))

    /* Languages ranked according to (3) */
    val langsRanked3: List[(String, Int)] = timed("Part 3: ranking using reduceByKey", rankLangsReduceByKey(langs, wikiRdd))

    println(langsRanked.head)
    /* Output the speed of each ranking */
    println(timing)
    sc.stop()
  }

  val timing = new StringBuffer
  def timed[T](label: String, code: => T): T = {
    val start = System.currentTimeMillis()
    val result = code
    val stop = System.currentTimeMillis()
    timing.append(s"Processing $label took ${stop - start} ms.\n")
    result
  }

//  val lst = sc.parallelize( [1, 2, 3, 4], 2 )


}

