import copy

class FragileDict:
    def __init__(self, dict = None):
        self._lock = True
        if dict is None:
            self._data = {}
        else:
            self._data = copy.deepcopy(dict)

    def __getitem__(self, key):
        if key in self._data:
            if self._lock:
                return copy.deepcopy(self._data[key])
            else:
                return self._data[key]
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if self._lock:
            raise RuntimeError("Protected state")
        else:
            self._data[key] = value

    def __contains__(self, key):
        if key in self._data:
            return True
        else:
            return False

    def __str__(self):
        return str(self._data) + ' ' + str(self._lock)

    def __enter__(self):
        self._lock = False
        self._old_data = copy.deepcopy(self._data)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._lock = True
        if exc_type is not None:
            print("Exception has been suppressed.")
            self._data = copy.deepcopy(self._old_data)
            del self._old_data
            return True
        self._data = copy.deepcopy(self._data)
        del self._old_data

if __name__ == "__main__":
    d = FragileDict({'key': []})

    with d:
        a = d['key']
        d['key'].append(10)
        a.append(10)

    a.append(10)
    print(a == [10, 10, 10] and d['key'] == [10, 10])
