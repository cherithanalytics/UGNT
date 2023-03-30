# UGNT-Trees/Trees

![cherithLogoBlue-100x100](https://user-images.githubusercontent.com/105679741/190519269-28c4bc1c-fb8f-4c8f-b119-8aa8188c98d6.png)
**UGNT Trees**

**Copyright © 2023 by Cherith Analytics**

The UGNT Trees are based upon the unfoldingWord® Greek New Testament (UGNT) text and morphology, version 0.27. The original work by unfoldingWord is available from [git.door43.org/unfoldingWord/el-x-koine_ugnt](https://git.door43.org/unfoldingWord/el-x-koine_ugnt). [unfoldingword.org/ugnt](https://www.unfoldingword.org/ugnt).

References on UGNT are available from unfoldingWord at [unfoldingword.org/ugnt](https://www.unfoldingword.org/ugnt).

The morphological data (text, lemma, UGNT Strong's number, analysis) in the UGNT Trees comes directly from the unfoldingWord data, and so any issues with this data is the sole responsibility of unfoldingWord.  Cherith Analytics modified the data in a few places, which are documented in the Documentation folder, and so any issues with the modifications are the sole responsibility of Cherith Analytics.

The UGNT Trees are also heavily based on multiple Greek New Testament trees developed by [Global Bible Initiative, LLC](https://www.gbi.llc) for internal use. Issues related to syntax or other data in the UGNT Trees are the sole responsibility of Cherith Analytics and will be fixed in future releases.

## Trees Folder Content

**Trees/** - folder with the UGNT Trees
* **UGNT-Sentence-Trees/** - folder with UGNT sentence trees
* **UGNT-Verse-Trees/** - folder with UGNT verse trees
* **CSV/** - folder with CSV files generated from the UGNT Trees, corresponding to the UGNT-Sentence-Trees and UGNT-Verse-Trees folders

## Notes about CSV files

The CSV files are generated from the UGNT Trees using a modified script originally created by [James Tauber](https://jktauber.com/2015/07/02/converting-gbi-syntax-trees-dependency-analysis/).

The fields are separated by PIPES (`|`) and not commas (`,`) to avoid issues with unescaped or unexpected content commas in the data, for example, in this line there is a comma in the text content (`Παῦλος,`), and commas in the morph data (`N,,,,,NMS,`):

```csv
460010010011|Παῦλος,|None|CL|Cat="noun"|Id="9"|morphId="460010010011"|Unicode="Παῦλος,"|Lemma="Παῦλος"|Lang="G"|StrongNumber="G39720"|Morph="N,,,,,NMS,"|Case="Nominative"|Gender="Masculine"|Number="Singular"|English="Paul"
```

For most dependency-related applications, users will likely only need the first four columns, which contain traditional dependency information:

| token_id | text | head_id | relation |
| --- | --- | --- | --- |
| 460010010021 | κλητὸς | 460010010031 | adjp |
| 460010010031 | ἀπόστολος | 460010010011 | np |

Since not every token has identical values in the base data, all additional fields have the header of attribute name encoded directly (e.g., `Gender="Masculine"`), and the files themselves do not have headers.
