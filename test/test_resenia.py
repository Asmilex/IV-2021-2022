from review_set.resenia import Resenia
from review_set.conjunto_resenias import ConjuntoResenias
import os

def test_constructor_conjunto_resenias():
    review_set = ConjuntoResenias(None)
    assert(review_set != None)

def test_dataset_name(dataset):
    assert(os.path.isfile(dataset))

def test_carga_datos(dataset):
    review_set = ConjuntoResenias(None)
    review_set.carga_datos(dataset)
    assert(review_set.numero_resenias() >= 0)

def test_instancias_conjunto(conjunto_resenias):
    res = True
    for i in range(conjunto_resenias.numero_resenias()):
        review = conjunto_resenias.buscar_resenia_por_indice(i)
        res = res and isinstance(review, Resenia)
    assert(res)
    
def test_texto_resenia(r: Resenia):
    texto = r.texto
    assert(isinstance(texto, str) and len(texto) > 0)

def test_puntuacion_resenia(r: Resenia):
    puntuacion = r.puntuacion
    assert(isinstance(puntuacion, int) and puntuacion > 0 and puntuacion <= 5 )

def test_local_id_resenia(r: Resenia):
    local_id = r.local_id
    assert(isinstance(local_id, str) and len(local_id) > 0)


    


