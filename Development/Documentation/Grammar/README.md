# UGNT-Trees
These are trees based upon the Unlocked Greek New Testament (UGNT) text and morphology. UGNT data and reference material below:

1. [UGNT Original Data](https://git.door43.org/unfoldingWord/el-x-koine_ugnt)
2. [UGNT References](https://www.unfoldingword.org/for-translators/content#UGNT)

Documentation/ - folder for documentation
  * UGNT/ - folder with files used to do automatic adjust of trees from NA28 to UGNT
  * ErrorReports/ - folder with files generated to report errors as well as documentation of how errors were fixed
    - Errors.CheckMorphDataAgainstTextUGNT.txt - lists the inconsistent (not perfect string match) between what is in the text file "ugnt.normalized.test.txt" and what is in "ugnt.normalized-edited.tsv"
    - Errors.CheckStrong2LemmaDataUGNT.txt - lists the inconsistent (not one-to-one mapping) between UGNT Strong's Number and UGNT lemma in "ugnt.normalized-edited.tsv"
    - Errors.CheckStrongAnalysis2LemmaDataUGNT.txt - lists the inconsistent (not one-to-one mapping) between UGNT Strong's Number + Analysis and UGNT lemma in "ugnt.normalized.test-edited.tsv"
    - Errors.CheckTreesAgainstMorphData.txt - lists the inconsistencies between the terminal node morphId and Unicode against the UGNT morph data
    - Errors.CheckTreeStructure.txt - lists the inconsistencies in structure and node categories to the grammar
    - Errors.CheckRulesNamesAndHeads.txt - lists the in structure that has an incorrect rule name/head as well as rules that could be used.
  * catDiff_modifications_edited.txt - has the documentation on the manual edits of the trees after doing the modifications documented in "tree_modifications_edited.txt"
  * catDiff_modifications_edited-unfixed - documents changes to undo the fixes that removed num/nump from the trees during previous manual editing
  * Errors.CheckTreesAgainstMorphData-2022.07.15-modifications-edited.txt - has the documentation on the manual edits of the trees after doing the modifications documented in catDiff_modifications_edited.txt and based upon the errors in Errors.CheckTreesAgainstMorphData.txt.
  * Errors.CheckTreesAgainstMorphData-2022.07.15-modifications-edited-unfixed.txt - documents changes to undo the fixes that removed num/nump from the trees during previous manual editing
  * greekgrammarNA28122319.cs - grammar used to create the NA28 trees, last modified on 12/23/2019.
  * greekgrammarUGNT.cs - modified version of the grammar used to create NA28 trees to accomodate differences in UGNT morphology and text
  * NotesOnSystemticIssues.txt - notes on issues that came up during the manual modification
  * tree_modifications_edited.txt - has the documentation on the manual edits of the trees after automatic adjustment based upon differences automatically generated
  * tree_modifications_edited-unfixed.txt - documents changes to undo the fixes that removed num/nump from the trees during previous manual editing
  * NA28_num_fixed - documents the changes made examining all occurances of num in NA28 and the corresponding words in UGNT to restore num/nump in the UGNT trees.
  * tree_modifications_during_auto_fix_tree_effort.txt - documents the modifications that needed to be manually made to the trees that were not appropriate to do automatically. This included clear errors during previous auto correction or manual editing that have nothing directly to do with the new UGNT morphology.
  * tree_modifications_FixRuleNamesAndHeads - documents the modifications that needed to be manually made to the trees that were not appropriate to do automatically. This included clear errors during previous auto correction or manual editing that have nothing directly to do with the new UGNT morphology.

NA28VerseTrees/ - folder for trees based off of NA28 text and morphology

UGNTVerseTrees-Auto/ - folder for trees that were created automatically from NA28 but using UGNT text and morphology

UGNTVerseTrees/ - folder for the most recent version of modified trees based off of UGNT text and morphology. It currently contains the version that has a consistent structure and node categories to the grammar in greekgrammarUGNT.cs.
 * Version2_diff_pass2/ - folder contains modified trees after modifications documented in tree_modifications_edited.txt
 * Version3_catDiff_pass1/ - folder contains modified trees after modifications documented in catDiff_modifications_edited.txt
 * Version5_tree_terminals_checked_pass2 - folder contains the modified trees after modifications documented in Errors.CheckTreesAgainstMorphData-2022.07.15-modifications-edited.txt
 * Version6_unfixed_num_nump - folder contains the modified trees after manuall unfixing the manual or auto changes that had previously removed num/nump from the trees.
 * Version7_for_structure_auto_fixes - folder contains the modified trees that have changes that are not appropriate to do automatically since they involve errors from previous auto or manual changes, and have nothing to do with the differences between NA28 and UGNT morphology. Used as input to the auto fix structure methods.
 * Version8_for_rules_auto_fill - folder contains the modified trees that have changes that are not appropriate to do automatically since they involve errors from previous auto or manual changes, and have nothing to do with the differences between NA28 and UGNT morphology. Used as input to the auto fix structure methods.
 * UGNT_Fixed_Struture - folder contains the resulting trees after both manual and auto fixing of tree structure.
 * UGNT_Fixed_RulesAndHead - folder contains the resulting trees after manual fixing of tree structure and auto checking and filling of rule names and heads.
