#  Spelling Bee Solver
This is a repo that solve the NY Times Spelling Bee. An app is created in Gradio which can be run locally.

## How it works
There are 7 letters which can be used multiple times within a word. The yellow letter to be used at least once in every word that is created. The format can be seen below: 

<img src="https://user-images.githubusercontent.com/1526881/114287844-4196d600-9a1f-11eb-86ca-3aae4f0a8f2d.png" width="150">

This solver filters an English dictionary for every word that contains the yellow letter. Then it iterates through the remaining words and uses Python sets to work out if the correct letters have been used in the word. All the words remaining are then displayed in a dataframe. 

## HuggingFace Link
https://huggingface.co/spaces/bradley6597/Spell-Bee-Solver

