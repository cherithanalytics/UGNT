# Trees

![cherithLogoBlue-100x100](https://user-images.githubusercontent.com/105679741/190519269-28c4bc1c-fb8f-4c8f-b119-8aa8188c98d6.png)
**CherithAnalytics Unlocked Greek New Testament Trees**

**Copyright © 2022 by Cherith Analytics**

The UGNT Trees are based upon the unfoldingWord® Greek New Testament (UGNT) text and morphology, version 0.27. The original work by unfoldingWord is available from [git.door43.org/unfoldingWord/el-x-koine_ugnt](https://git.door43.org/unfoldingWord/el-x-koine_ugnt). [unfoldingword.org/ugnt](https://www.unfoldingword.org/ugnt).

References on UGNT are available from unfoldingWord at [unfoldingword.org/ugnt](https://www.unfoldingword.org/ugnt).

The morphological data (text, lemma, UGNT Strong's number, analysis) in the UGNT Trees comes directly from the unfoldingWord data, and so any issues with this data is the sole responsibility of unfoldingWord.  Cherith Analytics modified the data in a few places, which are documented in the Documentation folder, and so any issues with the modifications are the sole responsibility of Cherith Analytics.

The UGNT Trees are also based on the unreleased Greek New Testament trees developed by GBI.LLC. Issues related to syntax or other data in the UGNT Trees are the sole responsibility of Cherith Analytics and will be fixed in future releases.

Below is the description of the Trees folder:

**XXXCCC.trees.xml** - tree files with trees for book XXX of the New Testament and chapter CCC in XML format.
  * XXX
```
{"Mat", 40 },
            {"Mrk", 41 },
            {"Luk", 42 },
            {"Jhn", 43 },
            {"Act", 44 },
            {"Rom", 45 },
            {"1Co", 46 },
            {"2Co", 47 },
            {"Gal", 48 },
            {"Eph", 49 },
            {"Php", 50 },
            {"Col", 51 },
            {"1Th", 52 },
            {"2Th", 53 },
            {"1Tm", 54 },
            {"2Tm", 55 },
            {"Tit", 56 },
            {"Phm", 57 },
            {"Heb", 58 },
            {"Jms", 59 },
            {"1Pe", 60 },
            {"2Pe", 61 },
            {"1Jn", 62 },
            {"2Jn", 63 },
            {"3Jn", 64 },
            {"Jud", 65 },
            {"Rev", 66 },
```
  * CCC - three digit with leading zeros for the chapter number.

**README.md** - this file


Below is the description of the content of each tree file.

**Tree Structure and Content**


```
The morphId is a CherithAnalytics created index to the instance based morphology.
The morphId is 12 digits with the format BBCCCVVVWWWP where:
    BB = two digits with leading zeros for the book (with 40 for Matthew)
    CCC = three digits with leading zeros for the chapter number
    VVV = three digits with leading zeros for the verse
    WWW = three digits with leading zeros for the word
    P = one digit for the part of the word
```
