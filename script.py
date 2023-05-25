# importing required modules
from PyPDF2 import PdfReader
from unidecode import unidecode
import json

# creating a pdf reader object
reader = PdfReader('./input/2020_RECIBO_DE_PAGAMENTO.pdf')

# printing number of pages in pdf file
# print(len(reader.pages))

for page in reader.pages:
    
    # extracting text from page
    text = page.extract_text()

    lst = text.splitlines()

    lst1 = lst[:45]
    lst2 = lst[-14:]
    lst3 = lst[45:-14]

    dic = {
        'doc': lst[0].strip()
    }

    dic.update(dict(zip([unidecode(e).strip().replace(':','') for e in lst1[1:6]], [unidecode(e).strip() for e in lst1[6:11]])))
    dic.update(dict(zip([unidecode(e).strip().replace(':','') for e in lst1[11:13]], [unidecode(e).strip() for e in lst1[13:15]])))
    dic.update(dict(zip([unidecode(e).strip().replace(':','') for e in lst1[15:18]], [unidecode(e).strip() for e in lst1[18:21]])))
    dic.update(dict(zip([unidecode(e).strip().replace(':','') for e in lst1[21:24]], [unidecode(e).strip() for e in lst1[24:27]])))
    dic.update(dict(zip([unidecode(e).strip().replace(':','') for e in lst1[27:29]], [unidecode(e).strip() for e in lst1[29:31]])))
    dic.update(dict(zip([unidecode(e).strip().replace(':','') for e in lst1[31:33]], [unidecode(e).strip() for e in lst1[33:35]])))
    dic.update(dict(zip([unidecode(e).strip().replace(':','') for e in lst1[35:40]], [unidecode(e).strip() for e in lst1[40:45]])))

    dic.update({unidecode(lst2[0]).strip().replace(':',''): lst2[1].strip()})
    dic.update({unidecode(lst2[2]).strip().replace(':',''): lst2[3].strip()})
    dic.update({unidecode(lst2[4]).strip().replace(':',''): lst2[5].strip()})
    dic.update(dict(zip([unidecode(e).strip().replace(':','') for e in lst2[6:10]], [unidecode(e).strip() for e in lst2[10:14]])))

    x = {
        "Extrato": []
    }

    if lst3[5] == '00005':
        lst3.insert(9, '')

    for i in range(int(len(lst3) / 5) - 1):
        i1 = (i + 1) * 5
        i2 = (i + 2) * 5
        x['Extrato'].append(dict(zip([unidecode(e).strip().replace(':','') for e in lst3[0:5]],[unidecode(e).strip() for e in lst3[i1:i2]])))

    dic.update(x)

    # Serialize dictionary to JSON string
    json_data = json.dumps(dic, indent=4)

    filename = dic['Referencia'][-4:] + dic['Referencia'][0:2] + '_' + dic['doc'].replace(' ','_')

    # Save JSON data to a file
    with open('./output/' + filename + '.json', 'w') as file:
        file.write(json_data)
