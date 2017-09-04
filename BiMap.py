import collections
def quickBiMap(dct):
    '''
    takes a dictionary, makes it bi-directional by reversing and appending its
    reversed form to the end
    '''
    rev = dict([reversed(pair) for pair in dct.items()])
    return {**dct, **rev}


class BiMap(dict):
    """
    2 keys can map to the same value
    """
    def __init__(self, *args, **kwargs):
            super(BiMap, self).__init__(*args, **kwargs)
            self.inverse = {}
            for key, value in self.items():
                    self.inverse.setdefault(value,[]).append(key) 

    def __setitem__(self, key, value):
            super(BiMap, self).__setitem__(key, value)
            self.inverse.setdefault(value,[]).append(key)        

    def __delitem__(self, key):
            self.inverse.setdefault(self[key],[]).remove(key)
            if self[key] in self.inverse and not self.inverse[self[key]]: 
                    del self.inverse[self[key]]
            super(BiMap, self).__delitem__(key)


class BiMapIFace(collections.abc.MutableMapping):
    '''
    Values need to be strings or ints, or you'll break it.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._inverse = {}
        self._store = dict(*args, **kwargs)
        for k,v in self.items():
            self._inverse.setdefault(v,[]).append(key)

    def __getitem__(self, key):
        try:
            return self._store[key]
        except KeyError:
            return self._inverse[key]
        else:
            raise

    def __setitem__(self, key, value):
        self._store[key] = value
        self._inverse[value] = key

    def __delitem__(self, key):
        del self._inverse[self.store[key]]
        del self._store[key]

    def __iter__(self):
        return iter(**{self._store}, **{self._inverse})

    def __len__(self):
        return len(self._store) + len(self._inverse)
