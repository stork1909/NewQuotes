from entries import create_entries

def create_form_template(entries_list, form_templates):
    current_template = [entries_list[0]]

    for i in range(1, len(entries_list)):
        prev = entries_list[i-1]
        curr = entries_list[i]

        if (
            prev['producer'] == curr['producer']
            and prev['product'] == curr['product']
        ):
            current_template.append(curr)
        else:
            form_templates.append(current_template)
            current_template = [curr]

    # последний блок
    form_templates.append(current_template)
    return form_templates

data = create_entries()
del data[-1]
forms = []

forms = create_form_template(data, forms)
for form in forms:
    for dict in form:
        print(dict['producer'], dict['product'], dict['size'])
    print()