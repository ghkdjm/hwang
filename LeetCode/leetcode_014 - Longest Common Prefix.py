def longestCommonPrefix(strs):
    strs = sorted(strs)
    first_str, last_str = strs[0], strs[-1]
    result = []
    for i in range(len(first_str)):
        if i < len(last_str):
            if first_str[i] == last_str[i]:
                result.append(first_str[i])
            else: break
        else: break
    result = "".join(result)
    return result