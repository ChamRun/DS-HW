def is_empty(stack):
    if len(stack) == 0:
        return True
    return False


def reverse(stack):
    top_element = stack.pop()
    if not is_empty(stack):
        reversed_stack = reverse(stack)

    return


if __name__ == '__main__':
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    reverse(stack)
