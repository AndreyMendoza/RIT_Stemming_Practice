from Code.Indexer import *
import time


def main():
    start = time.clock()

    collection_path = 'E:\\spanish_billion_words'
    idx = Indexer(collection_path)
    idx.read_collection(1)

    print('Finalizado!\nDuracion: ', (time.clock() - start) / 1, ' minutos.')

main()

