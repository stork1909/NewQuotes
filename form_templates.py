from entries import create_entries
import pickle

def create_form_template(entries_list, form_templates):
    current_template = []
    # print(len(entries_list))
    for i in range(1, len(entries_list)):
        current_producer = entries_list[i-1]['producer']
        current_product = entries_list[i-1]['product']
        next_producer = entries_list[i]['producer']
        next_product = entries_list[i]['product']
        if i == 1:
            current_template.append(entries_list[i-1])
            # print(f'added {i} {entries_list[i-1]["producer"]} {entries_list[i-1]["product"]} {entries_list[i-1]["size"]}')
        elif current_producer == next_producer and current_product == next_product:
            current_template.append(entries_list[i-1])
            # print(f'added {i} {entries_list[i-1]["producer"]} {entries_list[i-1]["product"]} {entries_list[i-1]["size"]}')
        else:
            current_template.append(entries_list[i-1])
            # print(f'added {i} {entries_list[i-1]["producer"]} {entries_list[i-1]["product"]} {entries_list[i-1]["size"]}')
            form_templates.append(current_template)
            current_template = []
    current_template.append(entries_list[-1])
    form_templates.append(current_template)
    return form_templates


data = create_entries()
del data[-1]
forms = []

forms = create_form_template(data, forms)

"""
for form in forms:
    for dict in form:
        print(dict['producer'], dict['product'], dict['size'])
    print()
"""

with open("samples/forms", "wb") as f:
    pickle.dump(forms, f)
