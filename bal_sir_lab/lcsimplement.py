from time import time

def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n + 1) for k in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

def backTrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return backTrack(C, X, Y, i-1, j-1) + X[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return backTrack(C, X, Y, i, j-1)
        else:
            return backTrack(C, X, Y, i-1, j)


def func(X,Y):
 start = time()
 C = LCS(X, Y)
 lcs = backTrack(C, X, Y,len(X), len(Y))
 end = time()
 timeq = end - start
 print("%d                  %s                  %f" %(C[len(X)][len(Y)], lcs , timeq)  )



print("Length             LCS                   TIme taken")
func("AATCFSTYWERDJC","ACACWTERGERDFG")
func("BDRRSSDFTYSKCB","BDCFSWETWEEADB")
func("XJIWFDSTGASDRU","XCWETDASASFUJI")
func("SDFWWTYWRTASDE","ASDASDFATMMQER")
func("IYWERWTYRTSHDL","AHIWERTFGOPPAY")
func("PIWERUWTGUIUNM","AUMGHWRTSDQWER")
func("EFWREGTRWYDAFF","EDFCWTSAFRGHKG")
func("ABCWRTRTHSDFSD","ACAASDFTUERTCG")
func("GRTWGWYWTSDFUH","ACACGWEASDFRTW")
func("ASDFWERWRTWDSF","ASDWWFTYIUFDSP")

