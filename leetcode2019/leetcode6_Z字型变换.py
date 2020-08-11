def convert(s: str, numRows: int) -> str:
    if not s:
        return s
    if numRows==1:
        return s
    
    c = (len(s)-numRows)//(2*numRows-2)+1
    lastrow = [numRows+i*(2*numRows-2)-1 for i in range(c+1)]
    firstrow = [last-(numRows-1) for last in lastrow]
    res = [s[first] for first in firstrow if first <= len(s)-1]

    for i in range(1, numRows-1):
        for last in lastrow:
            if last - (numRows-(i+1))>=0 and last - (numRows-(i+1)) <= len(s)-1:
                res.append(s[last - (numRows-(i+1))])
            if last + (numRows-(i+1)) <= len(s)-1:
                res.append(s[last + (numRows-(i+1))])

    res.extend([s[last] for last in lastrow[:-1]])
    return ''.join(res)

print(convert("PAYPALISHIRING", 4))
# "PINALSIGYAHRPI"