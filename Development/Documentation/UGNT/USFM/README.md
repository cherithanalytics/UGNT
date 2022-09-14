<img src="https://cdn.door43.org/assets/uw-icons/logo-ugnt-256.png" alt="drawing" width="100"/>

# unfoldingWord® Greek New Testament (UGNT)

*An open-licensed, lexically tagged, morphologically parsed critical Greek New Testament with full apparatus. It enables the global Church to have access to the original texts of the New Testament.*

## Basis

The UGNT text is based on the [Bunning Heuristic Prototype Greek New Testament (BHP)](https://git.door43.org/Door43/BHP). See the full rationale for the BHP text [here](https://git.door43.org/Door43/BHP/src/master/BHP.pdf). Also, see https://www.greekcntr.org for more information.

## Changes from the BHP

The UGNT text differs from the BHP in only a few respects, which are:

* Versification—The versification system used by the UGNT matches that of our [ULT](https://git.door43.org/unfoldingWord/en_ult). Currently, there is one difference:
  * BHP *does not* have Acts 19:41 but UGNT does (see [this commit](https://git.door43.org/Door43/UGNT/commit/9bb309780ad21ca9d26e5155a716437f004c4577)).
* Whole Verse Additions—The text of the UGNT is identical to the BHP except that we include several verses that the BHP omits. These are wrapped in single brackets [like this]. The full list of verses that we include are:
  * Matthew 16:3; 17:21; 18:11; 23:14
  * Mark 7:16; 9:44; 9:46; 11:26; 15:28; 16:9-20
  * Luke 17:36; 22:43-44; 23:17
  * John 5:4; 7:53; 8:1-11
  * Acts 8:37; 15:34; 24:7; 28:29
  * Romans 16:24
* Partial Verse Additions—We are compiling a list of commonly used variants which we will include with existing verses. A list will be provided here when they are available.
* Metadata—The UGNT text includes various metadata to mark the text which create links to other content that our software uses. For example, we add links to our [translationWords](https://git.door43.org/Door43/en_tw) articles where appropriate (about 33,737 occurrences).
* We remove the English style quotation marks that the BHP has (see this [pull request](https://git.door43.org/unfoldingWord/UGNT/pulls/150)).

## Related projects

* [unfoldingWord® Greek Lexicon](https://git.door43.org/unfoldingWord/en_ugl)
* [unfoldingWord® Literal Text](https://git.door43.org/unfoldingWord/en_ult)
