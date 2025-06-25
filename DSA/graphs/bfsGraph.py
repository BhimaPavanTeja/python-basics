from collections import deque

# Define the graph structure
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["jonny", "thom"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# Define the mango seller condition
def person_is_seller(name):
    # Example logic: person's name ends with 'm'
    # return name[-1] == 'm'
    # i declared thom as mango seller
    return name == 'thom'

# BFS search function
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    print("No mango seller found.")
    return False

# Run the search starting from "you"
search("you")
