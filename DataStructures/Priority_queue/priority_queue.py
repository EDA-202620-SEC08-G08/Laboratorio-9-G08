from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe

def default_compare_lower_value(father_nodo, child_nodo):
    if pqe.get_priority(father_nodo)<= pqe.get_priority(child_nodo):
        return True
    return False
def default_compare_higher_value(father_nodo, child_nodo):
    if pqe.get_priority(father_nodo) >= pqe.get_priority(child_nodo) :
        return True
    return False

def new_heap(is_min_pq= True):
    heap = {"elements": al.new_list(),
            "size": 0,
            "cmp_function":None}
    al.add_first(heap["elements"], None)
    
    if is_min_pq:
        heap["cmp_function"] = default_compare_lower_value
    else:
        heap["cmp_function"] = default_compare_higher_value
    return heap
    
def priority (my_heap, father, child):
    return my_heap["cmp_function"](father,child)

def exchange(my_heap,pos_1,pos_2):
    elements = my_heap["elements"]
    al.exchange(elements, pos_1, pos_2)

def swim (my_heap, pos):
    if pos == 1:
        return 
    padre = pos//2
    father_nodo = al.get_element(my_heap["elements"], padre)
    child_nodo = al.get_element(my_heap["elements"], pos)
    if priority(my_heap, father_nodo, child_nodo) is not True:
        exchange(my_heap,padre, pos)
        swim(my_heap, padre)
        
def insert(my_heap, priority,value):
    al.add_last(my_heap["elements"], pqe.new_pq_entry(priority,value))
    my_heap["size"] += 1
    swim(my_heap,my_heap["size"])
    return my_heap
    
        
def size (my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    return my_heap["size"] == 0

def sink (my_heap, pos):
    hijo_izq = 2 * pos
    hijo_der = 2 * pos + 1

    if hijo_izq > my_heap["size"]:
        return

    mejor = hijo_izq
    if hijo_der <= my_heap["size"]:
        izq_nodo = al.get_element(my_heap["elements"], hijo_izq)
        der_nodo = al.get_element(my_heap["elements"], hijo_der)
        if not priority(my_heap, izq_nodo, der_nodo):
            mejor = hijo_der

    padre_nodo = al.get_element(my_heap["elements"], pos)
    mejor_nodo = al.get_element(my_heap["elements"], mejor)
    if not priority(my_heap, padre_nodo, mejor_nodo):
        exchange(my_heap, pos, mejor)
        sink(my_heap, mejor)
    
def remove(my_heap):
    if size(my_heap) == 0:
        return None
    resultado = al.get_element(my_heap["elements"], 1)
    exchange(my_heap, 1, size(my_heap))
    al.remove_last(my_heap["elements"])
    my_heap["size"] -=1
    sink(my_heap,1)
    return pqe.get_value(resultado)

def get_first_priority(my_heap):
    if size(my_heap) == 0:
        return None
    resultado = al.get_element(my_heap["elements"], 1)
    return pqe.get_priority(resultado)

def is_present_value(my_heap, value):
    for n in range (1, size(my_heap)+1):
        nodo = al.get_element(my_heap["elements"], n)
        if pqe.get_value(nodo) == value:
            return n
    return -1

def contains(my_heap, value):
    if is_present_value(my_heap, value) != -1:
        return True
    return False

def improve_priority(my_heap, priority, value):
    pos = is_present_value(my_heap, value)
    if pos == -1:
        return my_heap
    nodo = al.get_element(my_heap["elements"], pos)
    nodo = pqe.set_priority(nodo, priority)
    swim(my_heap,pos)
    return my_heap


    
    

