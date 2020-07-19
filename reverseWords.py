def reverseWords (s: str):
    str_list = s.split(' ')
    str_work = ''
    new_list = []
    for i in str_list:
        str_work = i.strip()
        new_list.append(str_work)
    result = ''
    new_list = [x for x in new_list if x != '']
    for word in reversed(new_list):
        result += word + ' '
    print(result.strip())

if __name__ == "__main__":
    s = input("Enter Any String: ")
    reverseWords(s)