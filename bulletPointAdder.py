import clipboard

text = clipboard.paste()
formatted_text = list(map(lambda value: '*' + value, text.split('\n')))
clipboard.copy('\n'.join(formatted_text))