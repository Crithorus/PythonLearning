# file = open('input.txt')
#
# file.close()
# same as above but with only 1 step

# multiple modes 'r' || 'w'
with open('input.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)   # reverse content of list
    with open('input.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
