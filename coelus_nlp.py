from pymystem3 import Mystem

mystem = Mystem()


def pred_or_adj(string):
    analyzed = mystem.analyze(string)
    special_cases = ['должен', 'должно', 'должна', 'должны']
    if 'ADV' in analyzed[2]['analysis'][0]['gr']:
        return analyzed[0]['text'] + ' ' + analyzed[2]['text']
    if 'дат' in analyzed[0]['analysis'][0]['gr']:
        return analyzed[0]['text'] + ' ' + analyzed[2]['text']
    if 'им' in analyzed[0]['analysis'][0]['gr'] and analyzed[2]['text'] in special_cases:
        return analyzed[0]['text'] + ' ' + analyzed[2]['text']
    if 'A=' in analyzed[2]['analysis'][0]['gr']:
        return analyzed[0]['text'] + ' ' + analyzed[2]['analysis'][0]['lex']
    else:
        return 'Невозможно распознать данную строку'


test_string = 'Я хорош'
file = open('result.txt', 'w')
file.write(pred_or_adj(test_string))
file.close()
