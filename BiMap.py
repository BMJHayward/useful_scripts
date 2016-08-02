def quickBiMap(dct):
    '''
    takes a dictionary, makes it bi-directional by reversing and appending its
    reversed form to the end
    '''
    rev = dict([reversed(pair) for pair in dct.items()])
    return {**dct, **rev}


class BiMap:
    """
    2 keys can map to the same value
    """
    def __init__(self, *args, **kwargs):
            super(BiMap, self).__init__(*args, **kwargs)
            self.inverse = {}
            for key, value in self.iteritems():
                    self.inverse.setdefault(value,[]).append(key) 

    def __setitem__(self, key, value):
            super(BiMap, self).__setitem__(key, value)
            self.inverse.setdefault(value,[]).append(key)        

    def __delitem__(self, key):
            self.inverse.setdefault(self[key],[]).remove(key)
            if self[key] in self.inverse and not self.inverse[self[key]]: 
                    del self.inverse[self[key]]
            super(BiMap, self).__delitem__(key)