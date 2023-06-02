import re
import docx
from unidecode import unidecode
import pandas as pd

# def convert_to_pdf(request):

#     if request.method == 'POST' and request.FILES:
#         document = request.FILES['upload']
#     # Adjust the paths and filenames according to your specific requirements
#         input_file = document
#         output_file = 'path/to/output.pdf'

#         # Set the PATH environment variable to include the directory containing 'soffice'
#         libreoffice_dir = 'path/to/libreoffice/directory'
#         env = os.environ.copy()
#         env['PATH'] = f"{libreoffice_dir}:{env['PATH']}"
#         sve = Files(File_name=document)
#         sve.save()

#         # Execute the LibreOffice command
#         command = ['soffice', '--headless', '--convert-to',
#                    'pdf', input_file, '--outdir', './']
#         print(subprocess.call(command, env=env))

#         return HttpResponse("Conversion to PDF complete!")
#     # Return a response to indicate success
#     # return HttpResponse("Conversion to PDF complete!")
#     return render(request, 'test.html')

def ref_deteducation(TEXT):
    def convert_to_sentence_case(string):
        return ' '.join([i[0].upper() + i[1:].lower() if len(i) > 1 else i for i in string.split('. )')[0].split()])

    Ref_Dict = {'Reference': [], 'Type_id': []}
    for i in docx.Document(TEXT).paragraphs:
        for j in [r'(&\s)?[A-Z][a-z]+\,\s[A-Z]\.(\s[A-Z]\.)?\s\(\d{4}(\,\s)?([A-Z][a-z]+)?\)']:
            if re.search(j, convert_to_sentence_case(unidecode(i.text))):
                Ref_Dict['Reference'].append(i.text)
                Ref_Dict['Type_id'].append('APA')
                break

        for j in [r'(.*)[a-z]+\.\s"(pp.)?(no.)?(\(\d{4}\)\:\s)?(\b\d{4}\b\.)?']:
            if re.search(j, convert_to_sentence_case(unidecode(i.text))):
                Ref_Dict['Reference'].append(i.text)
                Ref_Dict['Type_id'].append('Chicago')
                break

        for j in [r'(and\s)?([A-Z]+\,\s)?[A-Za-z]+(\s[A-Za-z]+)?(-[A-Za-z]+)?\,\s[A-Z]\.([A-Z]\.)?\,\s\d{4}\,?\.?\s',]:
            if re.search(j, unidecode(i.text)):
                Ref_Dict['Reference'].append(i.text)
                Ref_Dict['Type_id'].append('Harvard')
                break

        for j in [r'(.*)[A-Z][A-Za-z]+?\s[A-Z]+\.\s[A-Z]']:
            if re.search(j, unidecode(i.text)):
                Ref_Dict['Reference'].append(i.text)
                Ref_Dict['Type_id'].append('Vancouver')
                break

        for j in [r'(et\sal\.)?\s\"', r'(\.\s\")']:
            if re.search(j, unidecode(i.text)):
                Ref_Dict['Reference'].append(i.text)
                Ref_Dict['Type_id'].append('MLA')
                break
    # Ref = pd.DataFrame(pd.DataFrame.from_dict(Ref_Dict).groupby(['Reference'])[
    #                    'Type'].agg(lambda x: ', '.join(set(x)))).reset_index()

    return Ref_Dict
