import gradio as gr
import pandas as pd
import requests
import re
import json

english_dict = pd.read_csv("dictionary.txt",
                         header = None, 
                         sep = ' ', 
                        names = ['word'])
english_dict = english_dict.reset_index(drop = True)
english_dict = english_dict.dropna()

url = 'https://spellbee.org'
def spell_bee_solver(no_centre, centre):
    full_set = set(no_centre.lower() + centre.lower())
    spell_bee_solver = english_dict[english_dict['word'].str.contains(str(centre.lower()), regex = False)]
    final_words = list()
    for i in range(0, spell_bee_solver.shape[0]):
        words = spell_bee_solver['word'].iloc[i]
        words_set = set(words)
        if len(words_set - full_set) == 0:
            final_words.append(words)

    final_word_df = pd.DataFrame(final_words)
    final_word_df.columns = ['word']
    final_word_df['word_length'] = final_word_df['word'].str.len()
    final_word_df = final_word_df[final_word_df['word_length'] > 3]
    final_word_df = final_word_df.sort_values('word_length', ascending = False)
    return(final_word_df)

def get_spellbee_answers(x):
    content = requests.get(url)._content
    content = re.sub(".*window.game = ", "", str(content))
    content = re.sub("(.*?)\\;.*", "\\1", content)
    content = json.loads(content)
    valid_words = content['data']['dictionary']
    final_word_df = pd.DataFrame(valid_words, columns = ['word'])
    final_word_df['word_length'] = final_word_df['word'].str.len()
    final_word_df = final_word_df[final_word_df['word_length'] > 3]
    final_word_df = final_word_df.sort_values('word_length', ascending = False)
    return(final_word_df)

with gr.Blocks() as app:
    with gr.Row():
        no_centre = gr.Textbox(label = 'Letters Outside of Centre')
        centre = gr.Textbox(label = 'Centre Letter')
    with gr.Row():
        solve_button = gr.Button(value = 'Solve')
        get_today_answers = gr.Button(value = "Get Today's answers")
    with gr.Row():
        output_df = gr.DataFrame(headers = ['word', 'word_length'])
    solve_button.click(spell_bee_solver, inputs = [no_centre, centre], outputs = [output_df])
    get_today_answers.click(get_spellbee_answers, inputs = [no_centre], outputs = [output_df])

app.launch(debug = True, share = False)