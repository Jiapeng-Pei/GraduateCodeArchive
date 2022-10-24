def rotateLeft(h):
    assert isRed(h.right)
    x = h.right
    h.right = x.left
    x.left = h
    x.color = h.color
    h.color = RED
    return x

def rotateRight(h):
    assert isRed(h.left)
    x = h.left
    h.left = x.right
    x.right = h
    x.color = h.color
    h.color = RED
    return x

def flipColors(h):
    assert !isRed(h)
    assert isRed(h.left)
    assert isRed(h.right)
    h.color = RED
    h.left.color = BLACK
    h.right.color = BLACK
    
def put(h, key, val):
    if h == None:
        return Node(key, val, RED);
    cmp = key.compareTo(h.key)
    if cmp < 0:
        h.left = put(h.left, key, val)
    elif (cmp > 0):
        h.right = put(h.right, key, val)
    else:
        h.val = val
    
    if isRed(h.right) and !isRed(h.left):
        h = rotateLeft(h)
    if isRed(h.left) and isRed(h.left.left):
        h = rotateRight(h)
    if isRed(h.left) and isRed(h.right):
        flipColors(h)
    
    return h

def moveRedLeft(cur):
    flipColors(cur)
    if isRed(cur.right.left):
        cur.right = rotateRight(cur.right)
        cur = rotateLeft(cur)
        flipColors(cur)
    
    return cur

def moveRedRight(cur):
    flipColors(cur)
    if isRed(cur.left.left):
        cur = rotateRight(cur)
        flipColors(cur)
    
    return cur

def balance(cur):
    if isRed(cur.left) and isRed(cur.right):
        flipColors(cur)
    if isRed(cur.right) and not isRed(cur.left):
        cur = rotateLeft(cur)
    if isRed(cur.left) and isRed(cur.left.left):
        cur = rotateRight(cur)

def delete(key):   
    root = delete(root, key)
    root.color = BLACK;

def delete(cur: Node, key):
    if key < cur.key:
        if isRed(cur.left) or isRed(cur.left.left):
            cur = moveRedLeft(cur)
        cur.left = delete(cur.left, key)
    else:
        if isRed(cur.left):
            cur = rotateRight(cur)
        if key == cur.key and cur.right is None:
            return None
        if isRed(cur->right) or isRed(cur.right.left):
            cur = moveRedRight(cur)
        if key == cur.key:
            nxt = min(cur.right)
            cur.key = nxt.key
            cur.val = nxt.val
            cur.right = deleteMin(cur.right)
        else:
            cur.right = delete(cur.right, key)
             
    return balance(cur)