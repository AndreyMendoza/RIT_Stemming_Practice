import os
import sys
import re
import operator
from collections import Counter
from nltk.stem.snowball import SnowballStemmer


class Indexer:

# ----------------------------------------------------------------------------------------------------------------------

    def __init__(self, collection_path):
        self.vocabulary = Counter()
        self.prefixes = {}
        self.collection_path = collection_path
        self.file_names = []

        # Execute the logic
        # self.read_collection()

# ----------------------------------------------------------------------------------------------------------------------

    def read_collection(self, n_files=300):

        self.extract_file_names()
        self.file_names = self.file_names[0:n_files]

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                self.process_content(content)
        self.vocabulary = self.sort_dictionary(self.vocabulary, 0)[0]
        self.save_vocabulary()

# ----------------------------------------------------------------------------------------------------------------------

    def extract_file_names(self):

        # Extract all the folder names of the collection
        try:
            sub_dir = os.listdir(self.collection_path)
        except:
            sys.exit('El directorio de la coleccion no fue encntrado')

        # Extract file names inside each folder of the collection
        for dir in sub_dir:
            try:
                dir_path = self.collection_path + '\\' + dir
                file_names = os.listdir(dir_path)

                for file_name in file_names:
                    self.file_names += [dir_path + '\\' + file_name]
            except:
                continue

# ----------------------------------------------------------------------------------------------------------------------

    def process_content(self, content):

        regex = r'[a-zA-ZáéíóúüÁÉÍÓÚÜñÑ]+'
        content = content.lower()
        words = re.findall(regex, content)
        self.vocabulary += Counter(words)

# ----------------------------------------------------------------------------------------------------------------------

    def apply_stemming(self):

        stemmer = SnowballStemmer('spanish')


# ----------------------------------------------------------------------------------------------------------------------

    def save_vocabulary(self):
        file = open('Results\\words.txt', 'w')
        file.write(str(self.vocabulary))
        file.close()

# ----------------------------------------------------------------------------------------------------------------------

    def sort_dictionary(self, dict, value):

        '''
        Orders a dictionary by it's key or term, depending on the value inserted.
        :param dict: dictionary to be sorted
        :param value: wich value use to order the dictionary. 0 is by key and 1 by term.
        :return: tuple of list of tuples(key:term) and a dictionary object ordered.
        '''

        sorted_values = sorted(dict.items(), key=operator.itemgetter(value))
        result_dict = {}

        for tuple in sorted_values:
            result_dict[tuple[0]] = tuple[1]
        return result_dict, sorted_values

# ----------------------------------------------------------------------------------------------------------------------
