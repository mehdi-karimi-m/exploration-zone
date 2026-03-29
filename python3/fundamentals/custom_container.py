class TagCounter:
    def __init__(self):
        #When a class member start with __ python make it private.
        self.__items = {}

    def __getitem__(self, tag):        
        return self.__items[tag.lower()]
    
    def __setitem__(self, tag, count):
        tag = tag.lower()
        self.__items[tag] = self.__items.get(tag, 0) + count

    def __iter__(self):
        return iter(self.__items)
    
    def add(self, tag):
        tag = tag.lower()
        self.__items[tag] = self.__items.get(tag, 0) + 1

    def __len__(self):
        return len(self.__items)


tag_counter = TagCounter()

tag_counter.add("Python")
tag_counter.add("python")
tag_counter.add("python")

print(tag_counter["PYTHON"])

tag_counter["Karimi"] = 7

print(len(tag_counter))

for tag in tag_counter:
    print(f"{tag}: {tag_counter[tag]}")

#Even the self.__item is private but by using __dict__ you can access to all members of a class even privates.
print(tag_counter.__dict__)
print(tag_counter._TagCounter__items)

