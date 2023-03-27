# UGNT-Trees/Trees/UGNT-Sentence-Trees

![cherithLogoBlue-100x100](https://user-images.githubusercontent.com/105679741/190519269-28c4bc1c-fb8f-4c8f-b119-8aa8188c98d6.png)
**UGNT Trees**

**Copyright © 2023 by Cherith Analytics**

The UGNT Trees are based upon the unfoldingWord® Greek New Testament (UGNT) text and morphology, version 0.27. The original work by unfoldingWord is available from [git.door43.org/unfoldingWord/el-x-koine_ugnt](https://git.door43.org/unfoldingWord/el-x-koine_ugnt). [unfoldingword.org/ugnt](https://www.unfoldingword.org/ugnt).

References on UGNT are available from unfoldingWord at [unfoldingword.org/ugnt](https://www.unfoldingword.org/ugnt).

The morphological data (text, lemma, UGNT Strong's number, analysis) in the UGNT Trees comes directly from the unfoldingWord data, and so any issues with this data is the sole responsibility of unfoldingWord.  Cherith Analytics modified the data in a few places, which are documented in the Documentation folder, and so any issues with the modifications are the sole responsibility of Cherith Analytics.

The UGNT Trees are also heavily based on multiple Greek New Testament trees developed by [Global Bible Initiative, LLC](https://www.gbi.llc) for internal use. Issues related to syntax or other data in the UGNT Trees are the sole responsibility of Cherith Analytics and will be fixed in future releases.

# UGNT-Sentence-Trees Folder Content

**BBBsentugnt.xml** - file with sentence trees for each book (BBB) in XML format
  * BBB - three **LOWERCASE** characters for book BBB of the New Testament according to the list below:
```
BBB
Mat = Mathew
Mrk = Mark
Luk = Luke
Jhn = John
Act = Acts
Rom = Romans
1Co = 1 Corinthians
2Co - 2 Corinthians
Gal - Galations
Eph - Ephesians
Php - Philipians
Col - Colosians
1Th - 1 Theselonians
2Th - 2 Thesolnians
1Tm - 1 Timothy
2Tm - 2 Timothy
Tit - Titus
Phm - Philemon
Heb - Hebrew,
Jms - James
1Pe - 1 Peter
2Pe - 2 Peter
1Jn - 1 John
2Jn - 2 John
3Jn - 3 John
Jud - Jude
Rev - Revelations
```

**LICENSE.md** - the license for the UGNT Trees

**README.md** - this file

# Trees File Structure and Content

**Tree Structure**

* **Sentences** - the top node, which includes one child node for each sentence
* **Sentence** - the top node for each sentence
  - **ID** = attribute indicating the sentence identification using Cherith Analystics created SentenceId index
```
The SentenceId is the word range of the sentence (a sentence may span verses and chapters)
in the format BBBC1:V1:W1-C2:V2:W2:
    BBB =  three characters for book BBB of the New Testament according to the list above:
    C1 = first word's chapter number
    V1 = first word's verse number in its chapter
    W1 = first word's word number in its verse
    C2 = last word's chapter number (1-3 digits)
    V2 = last word's verse number in its chapter
    W2 = last word's word number in its verse
    [numbers are 1-3 digits]

Because words in the trees may be in a different order from the order they appear in the text, 
the first word of a sentence in the text is not necessarily the first word in a tree, and likewise, 
the last word of a sentence in the text is not necessarily the last word in a tree.
```
* **Trees** - node containing a child node for each variation of contiguous trees that span the verse (only one variation included in the released trees)
* **Tree** - node containinng child nodes for the contiguous trees that span the verse
* **Node** - the node of a tree that fully or partially spans the verse

**Tree Content**

*Non-Terminal Nodes* - Non-terminal nodes in the tree are all the nodes above terminal nodes.

* **Cat** - Category (UGNT's Part of Speech)
```
noun = noun
adj = adjective
det = determiner
pron = pronoun
verb = verb
intj = interjection
prep = preposition
adv = adverb
conj = conjunction
ptcl = particle
```
* **Id** - a unique number for each node in a tree, starting with 1 and incrementing by 1, going top-down, left-to-right through the tree
* **Rule** - The name of the grammar rule in Cherith Analytics grammar for New Testament Greek
* **Head** - The zero-based index (left-to-right) of the child node that is the semanitc head

*Terminal Nodes* - Terminal nodes in the tree are for each UGNT word. It includes attributes for:

* **Cat** - see the description above in Non-terminal nodes
* **Id** - see the description above in Non-terminal nodes
* **morphId** - the Cherith Analytics created index to the instance based morphology.
```
The morphId is 12 digits with the format BBCCCVVVWWWP where:
    BB = two digits for the book number (with 40 for Matthew)
    CCC = three digits with leading zeros for the chapter number
    VVV = three digits with leading zeros for the verse number
    WWW = three digits with leading zeros for the word number
    P = one digit for the part of the word
    
Because words in the trees may be in a different order from the order they appear in the text, 
the word number of a word, wich indicates the order it appears in the text, does not necessarily 
indicate the order the word appears in a tree.
```
* **Unicode** - Unicode of the UGNT text (includes punctuations)
* **Lemma** - Unicode of the UGNT lemma of the word
* **Lang** - Single character for the UGNT language of the text (currently always "G" for Greek)
* **StrongNumber** - UGNT Strong number in the format GNNNNN
  - G = specifies the language
  - NNNNN = five digits, where the first four digits is the traditional Strong's Number and the fifth digit is a specific UGNT subvariant designation
* **Morph** = the UGNT morphological analysis code (see unfoldingWord's documentation on UGNT morphology)
* Spelling out the UGNT morphological analysis code (the node attributes below are not always present in a particular instances of a terminal node)
  - **Type** : part of speech subtype
  - **Mood**
  - **Tense**
  - **Voice**
  - **Person**
  - **Case**
  - **Gender**
  - **Number**
