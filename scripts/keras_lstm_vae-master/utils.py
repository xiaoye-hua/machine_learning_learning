# encoding=utf-8
import numpy as np



def name_to_vec(name, maxlen, indices_for_chars):
    v = np.zeros(maxlen, dtype=int)
    null_idx = indices_for_chars['<NULL>']
    v.fill(null_idx)
    for i, c in enumerate(name):
        if i >= maxlen: break
        n = indices_for_chars.get(c, null_idx)
        v[i] = n
    v[min(len(name), maxlen-1)] = indices_for_chars['<END>']
    return v

def vec_to_name(vec, chars):
    name = ''
    for x in vec:
        char = chars[x]
        if len(char) == 1:
            name += char
        elif char == '<END>':
            return name
    return name
