import json, uuid, random

infile = "../hotpot/hotpot_train_v1.json"
hotpot = json.load(open(infile))
outdata = []
for h in hotpot:
    titles = ''
    context = ''
    sp_only = False
    if random.random() < 0.99 or len(outdata) > 9:
        continue
    if sp_only:
        for sp in h['supporting_facts']:
            for p in h['context']:
                if sp[0] == p[0]:
                    #print(p[1])
                    #print('************')
                    #print(sp[1])
                    #print('--------------------------------------------------')
                    if sp[1] < len(p[1]):
                        titles += ' <t> ' + sp[0] + ' </t> '
                        context += ' <t> ' + sp[0] + ' </t> ' + p[1][sp[1]]
    else:
        for p in h['context']:
            titles += ' <t> ' + p[0] + ' </t> '
            context += ' <t> ' + p[0] + ' </t> ' + ''.join(p[1])
    idx = h['_id']
    question = h['question']
    answers = [{'answer_start': context.find(h['answer']), 'text': h['answer']}]
    qas = [{'answers':answers, 'question': question, 'id': idx}]
    example = {'title': titles, 'paragraphs':[{'context':context, 'qas':qas}]}
    if context.find(h['answer']) > 0 and not h['answer'] in ['yes', 'no']:
        outdata.append(example)
    else:
        print(h['answer'])

data = {"data":outdata, "version": 1.1}
with open(infile + '.squadlike', "w") as f:
    json.dump(data, f)
    
