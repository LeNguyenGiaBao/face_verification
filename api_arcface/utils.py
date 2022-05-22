import numpy as np
import base64

def revert_from_base64(input):
    str_encode = str.encode(input)
    base64_decode = base64.b64decode(str_encode)
    emb = np.frombuffer(base64_decode, dtype=np.float32)

    return emb