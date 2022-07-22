# UGNT-Trees
These are trees based upon the Unlocked Greek New Testament (UGNT) text and morphology.

Documentation/ - folder for documentation
  * UGNT/ - folder with files used to do automatic adjust of trees from NA28 to UGNT
  * ErrorReports/ - folder with files generated to report errors as well as documentation of how errors were fixed
    - Errors.CheckMorphDataAgainstTextUGNT.txt - lists the inconsistent (not perfect string match) between what is in the text file "ugnt.normalized.test.txt" and what is in "ugnt.normalized-edited.tsv"
    - Errors.CheckStrong2LemmaDataUGNT.txt - lists the inconsistent (not one-to-one mapping) between UGNT Strong's Number and UGNT lemma in "ugnt.normalized-edited.tsv"
    - Errors.CheckStrongAnalysis2LemmaDataUGNT.txt - lists the inconsistent (not one-to-one mapping) between UGNT Strong's Number + Analysis and UGNT lemma in "ugnt.normalized.test-edited.tsv"
    - Errors.CheckTreesAgainstMorphData.txt - lists the inconsistencies between the terminal node morphId and Unicode against the UGNT morph data
  * catDiff_modifications_edited.txt - has the documentation on the manual edits of the trees after doing the modifications documented in "tree_modifications_edited.txt"
  * Errors.CheckTreesAgainstMorphData-2022.07.15-modifications-edited.txt - has the documentation on the manual edits of the trees after doing the modifications documented in catDiff_modifications_edited.txt and based upon the errors in Errors.CheckTreesAgainstMorphData.txt.
  * greekgrammarNA28122319 - grammar used to create the NA28 trees, last modified on 12/23/2019.
  * NotesOnSystemticIssues.txt - notes on issues that came up during the manual modification
  * tree_modifications_edited.txt - has the documentation on the manual edits of the trees after automatic adjustment based upon differences automatically generated

NA28VerseTrees/ - folder for trees based off of NA28 text and morphology

UGNTVerseTrees-Auto/ - folder for trees that were created automatically from NA28 but using UGNT text and morphology

UGNTVerseTrees/ - folder for the most recent version of modified trees based off of UGNT text and morphology
 * Version2_diff_pass2/ - folder containing modified trees after modifications documented in tree_modifications_edited.txt
 * Version3_catDiff_pass1/ - folder containing modified trees after modifications documented in catDiff_modifications_edited.txt
 * Version5_tree_terminals_checked_pass2 - folder containg the modified trees after modifications documented in Errors.CheckTreesAgainstMorphData-2022.07.15-modifications-edited.txt
