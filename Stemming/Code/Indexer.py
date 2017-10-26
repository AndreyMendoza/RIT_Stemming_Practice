import re
import os
import sys
import collections

class Indexer:

# ----------------------------------------------------------------------------------------------------------------------

    def __init__(self, collection_path):
        self.vocabulary = {}
        self.prefixes = {}
        self.collection_path = collection_path

        self.read_collection()

# ----------------------------------------------------------------------------------------------------------------------

    def read_collection(self):
        try:
            sub_dir = os.listdir(self.collection_path)
        except:
            sys.exit('El directorio de la coleccion no fue encntrado')

        for dir in sub_dir:
            try:
                file_names = os.listdir(self.collection_path + '\\' + dir)
            except:
                continue
            for file_name in file_names:
                with open(self.collection_path + '\\' + dir + '\\' + file_name, 'r', encoding='utf-8') as content_file:
                    content = content_file.read()
                    self.process_content(content)
                exit(1)

# ----------------------------------------------------------------------------------------------------------------------

    def process_content(self, content):

        regex = r'[a-zA-ZáéíóúüÁÉÍÓÚÜñÑ]+'
        words = re.findall(regex, content)
        words_aux = words[0].lower()
        words[0] = words_aux

        count = collections.Counter(words)


        file = open('Results\\words.txt', 'w')
        file.write(str(count))

        return 1