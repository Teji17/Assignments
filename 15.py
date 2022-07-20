def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Tejinderpal'))
print(add_tags('b', 'Singh'))
