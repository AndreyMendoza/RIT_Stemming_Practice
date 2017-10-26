from Code.Indexer import *


def main():
    collection_path = 'E:\\spanish_billion_words'
    idx = Indexer(collection_path)
    idx.read_collection()


main()

