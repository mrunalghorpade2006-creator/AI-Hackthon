def text_utility(text, operation):

    if operation == "uppercase":
        return text.upper()

    elif operation == "lowercase":
        return text.lower()

    elif operation == "reverse":
        return text[::-1]

    elif operation == "length":
        return len(text)

    else:
        return "Unknown operation"


print(text_utility("Hello World", "uppercase"))
print(text_utility("Hello World", "lowercase"))
print(text_utility("Hello World", "reverse"))
print(text_utility("Hello World", "length"))