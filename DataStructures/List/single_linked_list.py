def new_list():
    """
    
    Se crea una nueva lista con los siguientes atributos:

    first: Primer nodo de la lista, inicializado en None.
    last: Último nodo de la lista, inicializado en None.
    size: Tamaño actual de la lista, inicializado en 0.
        
    Returns: Lista vacía recien creada.
    Return type: single_linked_list
    """
    newlist = {
        'first': None,
        'last': None,
        'size': 0
    }
    return newlist

def get_element(my_list, pos):
    """
    Encuentra el elemento de una lista en una posición dada.
    
    Parámetros:
    my_list (single_linked_list): Lista de la cual se obtendrá el elemento.
    pos (int): Posición del elemento a obtener.
    
    Returns: Elemento en la posición dada.
    Return type: int
    """
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node['info']

def is_present(my_list, element, cmp_function):
    """
    Encunetra la posición en la lista de un elemento dado. En caso de no estar en la lista, se retorna -1.
    
    Parámetros:

    my_list (single_linked_list): Lista en la cual se buscará el elemento.
    element (any): Elemento a buscar.
    cmp_function (function): Función de comparación.
    
    Returns: Posición del elemento si está presente, -1 en caso contrario.
    Return type: int
    """
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(temp['info'], element) == 0:
            is_in_array = True
        else:
            count += 1
            temp = temp['next']
    
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista.
    Agrega un nuevo nodo al inicio de la lista y aumenta el tamaño de la lista en 1. 
    En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.
    
    Parámetros:
    
    my_list (single_linked_list): Lista a la cual se agregará el elemento.
    element (any): Elemento a agregar.
    
    Returns: Lista con el elemento agregado al inicio.
    Return type: single_linked_list
    """
    if my_list['first'] is not None:
        my_list['first']['next'] = my_list['first']
        my_list['first']['info'] = element
    else:
        my_list['first'] = {
            'next': None,
            'info': element
        }
        my_list['last'] = {
            'next': None,
            'info': element
        }
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.
    Agrega un nuevo nodo al final de la lista y aumenta el tamaño de la lista en 1.
    En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.
    
    Parámetros:
    
    my_list (single_linked_list): Lista a la cual se agregará el elemento.
    element (any): Elemento a agregar.
    
    Returns: Lista con el elemento agregado al final.
    Return type: single_linked_list
    """
    if my_list['first'] is not None:
        i = 0
        node = my_list['first']
        while i < size(my_list)-1:
            node = node['next']
            i += 1
        node['next'] = {
            'next': None,
            'info': element
        }
        my_list['last'] = node['next']
    else:
        my_list['first'] = {
            'next': None,
            'info': element
        }
        my_list['last'] = {
            'next': None,
            'info': element
        }
    my_list['size'] += 1
    return my_list

def size(my_list):
    """
    Retorna el tamaño de la lista.
    
    Parámetros:
    
    my_list (single_linked_list): Lista de la cual se obtendrá el tamaño.

    Returns: Tamaño de la lista.
    Return type: int
    """
    return my_list['size']

def first_element(my_list):
    """
    Retorna el primer elemento de una lista no vacía.
    
    Parámetros: 
    
    my_list (single_linked_list): Lista de la cual se obtendrá el primer elemento.

    Returns: Primer elemento de la lista.
    Return type: any
    """
    return my_list['first']['info']

def is_empty(my_list):
    """
    Verifica si la lista está vacía.
    Retorna True si la lista está vacía, en caso contrario retorna False.
    
    Parámetros:
    
    my_list (single_linked_list): Lista a verificar.

    Returns: True si la lista está vacía, False en caso contrario.
    Return type: bool
    """
    return my_list['size'] == 0

def last_element(my_list):
    """
    Retorna el último elemento de una lista no vacía.
    
    Parámetros:
    
    my_list (single_linked_list): Lista de la cual se obtendrá el último elemento.

    Returns: Último elemento de la lista.
    Return type: any
    """
    return my_list['last']['info']

def delete_element(my_list, pos):
    """
    Elimina el elemento en la posición pos, la cual debe ser igual o mayor a cero y menor al tamaño de la lista.
    
    Parámetros:
    
    my_list (single_linked_list): Lista de la cual se eliminará el elemento.
    pos (int): Posición del elemento a eliminar.

    Returns: Lista con el elemento eliminado.
    Return type: single_linked_list
    """
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    elif my_list['first'] is not None:
        node = my_list['first']
        i = 0
        while i < pos - 1:
            node = node['next']
            i += 1
        if node['next'] is not None:
            node['next'] = node['next']['next']
            my_list['size'] -= 1
        else:
            node['next'] = None
            my_list['size'] -= 1
        return my_list

def remove_first(my_list):
    """
    Elimina el primer elemento de la lista y disminuye el tamaño de la lista en 1.
    
    Parámetros:
    
    my_list (single_linked_list): Lista de la cual se eliminará el primer elemento.
    
    Returns: Element eliminado de la lista.
    Return type: any
    """
    if my_list['size'] > 0:
        element = my_list['first']['info']
        my_list['first'] = my_list['first']['next']
        my_list['size'] -= 1
        if my_list['size'] == 0:
            my_list['last'] = my_list['first']
    return element

def remove_last(my_list):
    """
    Elimina el último elemento de la lista y disminuye el tamaño de la lista en 1.
    
    Parámetros:
    
    my_list (single_linked_list): Lista de la cual se eliminará el último elemento.

    Returns: Element eliminado de la lista.
    Return type: any
    """
    if my_list['size'] == 1:
        element = my_list['first']['info']
        my_list['first'] = None
        my_list['last'] = my_list['first']
        my_list['size'] -= 1
    elif my_list['size'] > 1:
        node = my_list['first']
        i = 1
        while i < my_list['size'] - 1:
            node = node['next']
            i += 1
        element = node['info']
        node['next'] = None
        my_list['size'] -= 1
        my_list['last'] = node
    return element

def insert_element(my_list, element, pos):
    """
    Inserta el elemento en la posición pos, la cual debe ser igual o mayor a cero y menor o igual al tamaño de la lista.
    
    Parámetros:
    
    my_list (single_linked_list): Lista en la cual se insertará el elemento.
    element (any): Elemento a insertar.
    pos (int): Posición en la cual se insertará el elemento.
   
    Returns: Lista con el elemento insertado.
    Return type: single_linked_list
    """
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos == 0 and size(my_list) == 1:
        add_first(my_list, element)
        return my_list
    node = my_list['first']
    i = 0
    while i < pos:
        node = node['next']
        i += 1
    node['next'] = {
        'info': element,
        'next': node['next']
    }
    my_list['size'] += 1
    return my_list

def change_info(my_list, pos, new_info):
    """
    Cambia la información de un elemento en la posición dada por la información new_info.
    
    Parámetros:
    
    my_list (single_linked_list): Lista en la cual se cambiará la información del elemento.
    pos (int): Posición del elemento a cambiar.
    new_info (any): Nueva información del elemento.

    Returns: Lista con la información del elemento cambiada.
    Return type: single_linked_list
    """
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        node = my_list['first']
        i = 0
        while i < pos:
            node = node['next']
            i += 1
        node['info'] = new_info
        return my_list
    
def exchange(my_list, pos_1, pos_2):
    """
    Intercambia la posición de los elementos en las posiciones pos_1 y pos_2.
    
    Parámetros:
    
    my_list (single_linked_list): Lista en la cual se intercambiarán los elementos.
    pos_1 (int): Posición del primer elemento a intercambiar.
    pos_2 (int): Posición del segundo elemento a intercambiar.
    
    Returns: Lista con los elementos intercambiados.
    Return type: single_linked_list
    """
    if pos_1 < 0 or pos_1 > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos_2 < 0 or pos_2 > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos_1 == pos_2:
        return my_list
    else:
        node1 = my_list['first']
        node2 = my_list['first']
        i = 0
        j = 0
        
        while i < pos_1:
            node1 = node1['next']
            i += 1
        while j < pos_2:
            node2 = node2['next']
            j += 1
            
        #Determino cuál aparece primero que el otro:
        if pos_1 > pos_2:
            x = node1
            y = node2
        else: 
            x = node2
            y = node1
            
        #nodo anterior a 'y' y a 'x':
        node_a = my_list['first']
        k = 0
        while k < size(y) - 2:
            node_a = node_a['next']
            k += 1
        node_b = my_list['first']
        h = 0
        while h < size(x) - 2:
            node_b = node_b['next']
            h += 1
        #Asigno las nuevas posiciones:
        node_a['next'] = x
        node_b['next'] = x['next']
        x['next'] = y
        
        if x == my_list['last']:
            my_list['last'] = y
            y['next'] = None
        
        return my_list

def sub_list(my_list, pos, num_elements):
    """
    Retorna una sublista de la lista original que contiene num_elements elementos a partir de la posición pos.
    
    Parámetros:
    
    my_list (single_linked_list): Lista de la cual se obtendrá la sublista.
    pos (int): Posición inicial de la sublista.
    num_elements (int): Número de elementos de la sublista.

    Returns: Sublista de la lista original.
    Return type: single_linked_list
    """
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    if (pos+num_elements > size(my_list)) or (pos == size(my_list)-1 and num_elements > 1):
        raise Exception('IndexError: list index out of range')
    else:
        newlist = new_list()            
        i = 0
        node = my_list['first']
        while i < pos:
            node = node['next']
            i += 1
        newlist['first'] = node
        node2 = newlist['first']
        j = 1
        while j < num_elements:
            node2 = node2['next']
            add_last(newlist, node2['info'])
            j += 1
        newlist['size'] = j
        if node2 != my_list['last']:
            node2['next'] = None
        newlist['last'] = node2
        return newlist
