from Code.Indexer import *
import time


def main():

    # n_files = [1, 3, 6, 16, 40, 101, 303, 588, 1534, 4002, 9436]
    #
    # for n_file in n_files:
    n_file = 6
    print('Corriendo para ', str(n_file), '...', end='')
    start = time.clock()

    collection_path = 'E:\\spanish_billion_words'
    idx = Indexer(collection_path)
    idx.process_collection(str(n_file) + '_files', n_file)
    final_time = (time.clock() - start)

    print('Finalizado! Duracion:\n\tMinutos: ', final_time / 60, '\n\tSegundos:', final_time - start)

main()

