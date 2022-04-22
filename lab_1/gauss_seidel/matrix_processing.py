def diagonal_predominance_check(A):
    n = len(A)
    for i in range(n):
        if abs(A[i][i]) < sum(map(abs, A[i])):
            return False
    return True

def diagonal_predominance_status(A):
    n = len(A)
    max_values_index = []
    for i in range(n):
        if 2 * max(map(abs, A[i])) < sum(map(abs, A[i])):
            return False
        m = abs(A[i][0])
        index_m = 0
        for j in range(1, n):
            if abs(A[i][j]) > m:
                m = abs(A[i][j])
                index_m = j
        max_values_index.append(index_m)
    for i in range(n):
        for j in range(n):
            if i != j and max_values_index[i] == max_values_index[j]:
                return False
    return True

def diagonal_predominance_transform(A):
    n = len(A)
    tmp = []
    for i in range(n):
        m = max(map(abs, A[:, i]))
        for j in range(n):
            if A[j][i] == m:
                tmp.append(A[j])
    return tmp

def det(A):
    total = 0
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]
        sign = (-1) ** (fc % 2)
        sub_det = det(As)
        total += sign * A[0][fc] * sub_det
    return total

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])
    MC = zeros_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
    return MC

def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M