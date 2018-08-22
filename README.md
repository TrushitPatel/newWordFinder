# newWordFinder
nlp based project 
project :
this leverages nltk to process a subtitle to get new word(that is new for a person)

step:#1
  Remove all other used in subtitle(.srt file) other than words.
  1.numbers
  2.<tags>
  3.time sequence(includes numbers and : - > )
step:#2
  Remove stopWords
  stopwords=those words that are used in any sentences and used to support/as auxilliary or has no meaning for out task.
 1.get stop words from nltk
 2.i found from stack over flow
 3.punctuations
 4.shortenings
Step:#3
  remove commonWords
 1.get a list of common words according to your level(make/get a list of words that you know already)
 2.remove all their related/derived words.
  nltk corpus and stopwords
    1.stemming
    2.lemmitization
    3.plurals/singulars
    4.tense varients
 3.remove words that are representation of numbers
  inflect engine
    1.one/ two/ nineteen..
      number_to_word()
    2.first/ second /nineteenth..
      ordinal(number_to_word())
    3.twenty/ thirty/ forty..
      same
    4.twentieth/ thirtieth..
      same
    5.1 and 2 will take care of other numbers
 4.
