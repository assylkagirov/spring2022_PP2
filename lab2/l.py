def openclosed(S):
    arr = []
    for ch in S:
        if ch in ["(", "{", "["]:
            arr.append(ch)
        else:
            if not arr:
                return False
            cur_ch = arr.pop()
            if cur_ch == '(':
                if ch != ")":
                    return False
            if cur_ch == '{':
                if ch != "}":
                    return False
            if cur_ch == '[':
                if ch != "]":
                    return False
    if arr:
        return False
    return True
    
S = str(input())
if openclosed(S):
    print("Yes")
else:
    print("No")