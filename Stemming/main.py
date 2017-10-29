from Code.Indexer import *
import time


if __name__ == '__main__':

    argv = sys.argv[1:]

    if len(argv) >= 3:

        n_files = int(argv[0])
        results_name = argv[1]
        collection_path = argv[2]

        print('Procesando ', str(n_files), ' archivos...', end='')
        start = time.clock()

        idx = Indexer(collection_path)
        idx.process_collection(results_name, n_files)

        final_time = (time.clock() - start)
        print('Finalizado! Duracion:\n\tMinutos: ', final_time / 60, '\n\tSegundos:', final_time)

    else:
        sys.exit('La cantidad de parametros no es la correcta. Debe seguir el siguiente formato:\n\t' +
                         '-	python main.py num_documentos nombre_resultados ruta_coleccion')




