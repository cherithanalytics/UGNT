"""Return UGNT as a TSV like sample.tsv, i.e.
400010010011	βίβλος	pos:noun;case:nominative;gender:feminine;number:singular"""

import json
import os
import pandas as pd

# Hey Andi! This is the input file. Edit it to fit your ugnt file location.
ugnt_file = os.path.join('data', 'ugnt.normalized.tsv')

# The rest shouldn't need to be edited except possibly the output file location.
tsv = pd.read_csv(ugnt_file, delimiter='\t', names=['id', 'form', 'lemma', 'strongs', 'postags', 'gloss'])
pos_dict = {'N': ['noun', {'S': 'substantive_adj', 'P': 'predicate_adj'}],
            'A': ['adjective', {'A': 'ascriptive', 'R': 'restrictive'}],
            'E': ['determiner', {'A': 'article', 'D': 'demonstrative', 'F': 'differential', 'P': 'possessive',
                                 'Q': 'quantifier', 'N': 'number', 'O': 'ordinal', 'R': 'relative',
                                 'T': 'interrogative'}],
            'R': ['pronoun', {'D': 'demonstrative', 'P': 'personal', 'E': 'reflexive', 'C': 'reciprocal',
                              'I': 'indefinite', 'R': 'relative', 'T': 'interrogative'}],
            'V': ['verb', {'T': 'transitive', 'I': 'intransitive', 'L': 'linking', 'M': 'modal', 'P': 'periphrastic'}],
            'I': ['interjection', {'E': 'exclamation', 'D': 'directive', 'R': 'response'}],
            'P': ['preposition', {'I': 'improper'}],
            'D': ['adverb', {'O': 'correlative'}],
            'C': ['conjunction', {'C': 'coordinating', 'S': 'subordinating', 'O': 'correlative'}],
            'T': ['particle', {'F': 'foreign', 'E': 'error'}]}
mood_dict = {'I': 'indicative', 'M': 'imperative', 'S': 'subjunctive', 'O': 'optative', 'N': 'infinitive',
             'P': 'participle'}
tense_dict = {'P': 'present', 'I': 'imperfect', 'F': 'future', 'A': 'aorist', 'E': 'perfect', 'L': 'pluperfect'}
voice_dict = {'A': 'active', 'M': 'middle', 'P': 'passive'}
person_dict = {'1': '1st', '2': '2nd', '3': '3rd'}
case_dict = {'N': 'nominative', 'G': 'genitive', 'D': 'dative', 'A': 'accusative', 'V': 'vocative'}
gender_dict = {'M': 'masculine', 'F': 'feminine', 'N': 'neuter'}
number_dict = {'S': 'singular', 'P': 'plural'}
pos_texts = []

for postag in tsv['postags']:
    print(postag)
    pos = pos_dict[postag[0]][0]
    pos_text = f'pos:{pos}'
    if postag[1] != ',':
        pos_type = pos_dict[postag[0]][1][postag[1]]
        pos_text += f';type:{pos_type}'
    if postag[2] != ',':
        mood = mood_dict[postag[2]]
        pos_text += f';mood:{mood}'
    if postag[3] != ',':
        tense = tense_dict[postag[3]]
        pos_text += f';tense:{tense}'
    if postag[4] != ',':
        voice = voice_dict[postag[4]]
        pos_text += f';voice:{voice}'
    if postag[5] != ',':
        person = person_dict[postag[5]]
        pos_text += f';person:{person}'
    if postag[6] != ',':
        case = case_dict[postag[6]]
        pos_text += f';case:{case}'
    if postag[7] != ',':
        gender = gender_dict[postag[7]]
        pos_text += f';gender:{gender}'
    if postag[8] != ',':
        number = number_dict[postag[8]]
        pos_text += f';number:{number}'

    # There's also a 10th position. I don't know what it does.

    print(pos_text)
    pos_texts.append(pos_text)

print(len(tsv['postags']))
print(len(pos_texts))

d = {'id': tsv['id'], 'form': tsv['form'], 'pos_text': pos_texts}

new_df = pd.DataFrame(data=d)
print(new_df)

# This is where the new TSV file will be written to. Edit it to your liking.
new_df.to_csv(os.path.join('data', 'ugnt-morphs.tsv'), sep='\t', index=False, header=False)
