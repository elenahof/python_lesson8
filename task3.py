class NumListError(Exception):

    def __init__(self, list):
        self.list = list


def list_filter(line):
    if line.isdigit():
        return line
    else:
        try:
            float(line)
            return line
        except ValueError:
            raise NumListError(f"{line} is not a number!")


print("Enter the numbers using enter, write 'stop' to exit")
text = ''
list_num = []
while text != "stop":
    try:
        text = input()
        list_num.append(list_filter(text))
    except NumListError:
        if text != 'stop':
            print(NumListError)

print(list_num)