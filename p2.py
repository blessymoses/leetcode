"""
Given a string in the form AAAABBBBCCCCCDDEEEE,
compress it to become A4B4C5D2E4
"""


def compress_letters(s: str) -> str:
    if not len(s):
        return ""
    i = 0
    count = 1
    result = ""
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            count += 1
        else:
            result = result + s[i] + str(count)
            count = 1
        i += 1
    return result + s[i] + str(count)


print(compress_letters("AAAABBBBCCCCCDDEEEE"))
print(compress_letters("AAB"))
print(compress_letters("AAAaaa"))
print(f"Empty string: {compress_letters('')}")
print(compress_letters("A"))
