


def new_list():
    
    """Crea una lista (de tipo array_list) vacía.
    La lista es creada con los siguientes atributos:
    
        size: Tamaño actual de la lista, inicializado en 0.
        elements: Lista de elementos, inicializada en una lista vacía.

    Returns: Lista vacía recien creada.
    Return type: array_list
        
    """
    newlist = {
        "elements": [],
        "size": 0, 
    }
    return newlist




def get_element(my_list, index):
    """
    Retorna el elemento en la posición dada.

    Retorna el elemento en la posición pos, la cual debe ser igual o mayor a cero y menor al tamaño de la lista. 0 <= pos < size(my_list).
    Si la posición no es válida, lanza un error IndexError: list index out of range. Esta función no elimina el elemento de la lista.

        Parameters: - my_list (array_list) – Lista de la cual se obtendrá el elemento.
                    - pos (int) – Posición del elemento a obtener.

        Returns: Elemento en la posición dada.
        Return type: any 

    """
    
    return my_list["elements"][index]



def is_present(my_list, element, cmp_function):
    """
    Verifica si un elemento está presente en la lista.

    Parameters:
        my_list (array_list): Lista en la cual se buscará el elemento.
        element (any): Elemento a buscar.
        cmp_function (function): Función de comparación.

    Returns:
        Posición del elemento si está presente, -1 en caso contrario.
    Return type: int
    """
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista.



    Parameters: 
        my_list (array_list): Lista a la cual se le agregará el elemento.
        element (any): Elemento a agregar. 

    Returns: Lista con el elemento agregado al inicio.
    Return type: array_list
    """
    
    new_list = [0]*(my_list["size"] + 1)
    new_list[0] = element
    
    for i in range(0, my_list["size"]):
        new_list[i+1] = my_list["elements"][i]
    
    my_list["elements"] = new_list
    my_list["size"] += 1
    
    return my_list



def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.
    
    Parameters:
        my_list (array_list):  Lista a la cual se le agregará el elemento.
        element (any): Elemento a agregar.

    Returns: Lista con el elemento agregado al final. 
    Returns type: array_list
    """
    
    if my_list["size"] == 0:
        new_list = [element]
        my_list["elements"] = new_list 
    
    elif my_list["size"] == len(my_list["elements"]):
        new_list = [0]*(my_list["size"]*2)
        for i in range(0,my_list["size"]):
            new_list[i] = my_list["elements"][i]
        new_list[my_list["size"]] = element
        my_list["elements"] = new_list
        
    else:
        my_list["elements"][my_list["size"]] = element
    
    my_list["size"] += 1 
     
    return my_list




def size(my_list):
    """
    Retorna el tamaño de la lista.
    
    Parameters:
        my_list (array_list): Lista de la cual se obtendrá el tamaño.

    Returns: Tamaño de la lista.
    Returns type: int
    """
    return my_list["size"]
    


def first_element(my_list):
    """
    Retorna el primer elemento de una lista no vacía.
    
    Retorna el primer elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. Esta función
    no elimina el elemento de la lista.

    Parameters:
        my_list (array_list):  Lista de la cual se obtendrá el primer elemento.

    Returns: Primer elemento de la lista.
    Return type: any
    """
    
    return get_element(my_list, 0)



def last_element(my_list):
    """
    Retorna el último elemento de la lista no vacía.
    
    Retorna el último elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. Esta función
    no elimina el elemento de la lista.

    Parameters:
        my_list (array_list): Lista de la cual se obtendrá el último elemento.

    Returns: Último elemento de la lista.
    Return type: any
    """
    
    return get_element(my_list, (my_list["size"]-1))


                   

def is_empty(my_list):
    """
    Verifica si la lista está vacía.

    Parameters:
        my_list (_array_list):  Lista a verificar.
        
    Returns: True si la lista está vacía, False en caso contrario.
    Return type: bool
    """

    state = False
    
    if size(my_list) == 0:
        state = True
    
    return state



def delete_element(my_list, pos):
    """
    Elimina el elemento en la posición dada.

    Elimina el elemento en la posición pos, la cual debe ser igual o mayor a cero y menor al tamaño de la lista. 0 <= pos < size(my_list).
    Si la posición no es válida, lanza un error IndexError: list index out of range, esto lo hace llamando a la función get_element().



    Parameters:
        my_list (arra_list): Lista de la cual se eliminará el elemento.
        pos (int): Posición del elemento a eliminar.

    Returns: Lista con el elemento eliminado.
    Returns type: array_list 
    """
    
    if 0 <= pos < size(my_list):
        elem = my_list["elements"]
    
        for i in range(pos, size(my_list)-1):
            elem[i] = elem[i+1]
        my_list["elements"] = elem
        my_list["size"] -= 1
        
    else:
        return get_element(my_list, pos)
    
    return my_list


def remove_first(my_list):
    """
    Elimina el primer elemento de la lista.
    Elimina el primer elemento de la lista y disminuye el tamaño de la lista en 1. Si la lista está vacía, lanza un error 
    IndexError: list index out of range.

    Parameters:
        my_list (array_list): Lista de la cual se eliminará el primer elemento.

    Returns: Elemento recien eliminado.
    Return type: any
        
    """
    

    if  not (is_empty(my_list)):
        for i in range(0, size(my_list)-1):
            my_list["elements"][i] = my_list["elements"][i+1]
        my_list["size"] -= 1

        return first_element(my_list)
    

def remove_last(my_list):
    """
    Elimina el último elemento de la lista.
    
    Elimina el último elemento de la lista y disminuye el tamaño de la lista en 1. Si la lista está vacía, lanza un error 
    IndexError: list index out of range.

    Parameters:
        my_list (array_list): Lista de la cual se eliminará el último elemento.

    Returns: Elemento recien eliminado.
    Return type: any

    """
    
    if  not (is_empty(my_list)):
        
        my_list["elements"][size(my_list)-1] = None
        my_list["size"] -= 1
        
    
    return last_element(my_list)



def insert_element(my_list, elem, pos):
    """
    Inserta un elemento en la posición dada.

    Inserta el elemento en la posición pos. La lista puede estar vacia o tener elementos. Se incrementa el tamaño de la lista en 1.

    Parameters:
        my_list (array_list): Lista en la cual se insertará el elemento.
        elem (any): Elemento a insertar.
        pos (int): Posición en la cual se insertará el elemento.

    Returns: Lista con el elemento insertado.
    Return type: array_list
       
    """
    
    
    if is_empty(my_list):
        my_list = add_last(my_list, elem)
        
    elif pos == size(my_list):
        my_list = add_last(my_list,elem)
        
    else:
        new_list = [0]*(size(my_list)+1)
        for i in range(0, pos):
            new_list[i] = my_list["elements"][i]
        new_list[pos] = elem
        for i in range(pos, size(my_list)):
            new_list[i+1] = my_list["elements"][i]
        
        my_list["elements"] = new_list
        my_list["size"] += 1
        
    return my_list 
    
    
    
def change_info(my_list, pos, new_info):
    """
    Cambia la información de un elemento en la posición dada.

    Cambia la información del elemento en la posición pos por la información new_info. Si la posición no es válida,
    lanza un error IndexError: list index out of range.

    Args:
        my_list (array_list): Lista en la cual se cambiará la información del elemento.
        pos (int): Posición del elemento a cambiar.
        new_info (any): Nueva información del elemento.

    Returns: Lista con la información del elemento cambiada.
    Return type: array_list
        
    """
    
    if 0<= pos < size(my_list):
        my_list["elements"][pos] = new_info
        return my_list
    else:
        return get_element(my_list, pos)
        
    
        
def exchange(my_list, pos_1, pos_2):
    """
    Intercambia la información de dos elementos en las posiciones dadas.

    Intercambia la información de los elementos en las posiciones pos_1 y pos_2. Si alguna de las posiciones no es válida,
    lanza un error IndexError: list index out of range.

    Args:
        my_list (arra_list):  Lista en la cual se intercambiará la información de los elementos.
        pos_1 (int): Posición del primer elemento a intercambiar.
        pos_2 (int): Posición del segundo elemento a intercambiar.

    Returns: Lista con la información de los elementos intercambiada.
    Return type: array_list
    """
    if (0<= pos_1 < size(my_list)) and (0<= pos_2 < size(my_list)):
        info_pos_1 = get_element(my_list, pos_1)
        info_pos_2 = get_element(my_list, pos_2)
        my_list = change_info(my_list, pos_1, info_pos_2)
        my_list = change_info(my_list, pos_2, info_pos_1)
    else:
        return get_element(my_list, size(my_list))
    
    return my_list



def sub_list(my_list, pos_i, num_elements):
    if 0 <= pos_i < num_elements:
        new_list = { "elements": [0]*num_elements,
                  "size": num_elements
                  }
        i = 0
        elem_pos = pos_i
        while i < num_elements:
            new_list = add_last(new_list, my_list["elements"][elem_pos])
            i += 1
            elem_pos += 1
    else:
        return get_element(my_list, pos_i)
    
    return new_list
            
    
        
        
