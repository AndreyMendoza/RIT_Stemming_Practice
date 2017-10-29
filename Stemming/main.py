from Code.Indexer import *
import time


def main():
    start = time.clock()

    collection_path = 'E:\\spanish_billion_words'
    idx = Indexer(collection_path)
    idx.process_collection('1_file', 3)

    print('Finalizado!\nDuracion: ', (time.clock() - start) / 1, ' minutos.')

main()

