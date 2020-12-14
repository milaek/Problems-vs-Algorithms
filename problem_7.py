# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, home, not_found):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(home)
        self.not_found_handler = not_found

    def insert(self, route, handler):
        # Similar to our previous example you will want to add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for part in route:
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                current_node.insert(part, self.not_found_handler)
                current_node = current_node.children[part]
        current_node.handler = handler

    def find(self, route):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.point(route)
        if current_node is None:
            return None
        return current_node.handler

    def point(self, route):
        # helper function to point to required node within the trie
        current_node = self.root
        for path in route:
            if path in current_node.children:
                current_node = current_node.children[path]
            else:
                return None
        return current_node


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, part, handler):
        # Insert the node as before
        self.children[part] = RouteTrieNode(handler)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, home, not_found):
        # Create a new RouteTrie for holding our routes
        self.trie = RouteTrie(home, not_found)

    def add_handler(self, path, handler):
        # Add a handler for a path
        route = self.splitter(path)
        self.trie.insert(route, handler)

    def lookup(self, path):
        # lookup path and return the associated handler
        # return the "not found" handler if not found
        route = self.splitter(path)
        lookup_val = self.trie.find(route)
        if lookup_val is None:
            return "404 page not found"
        return lookup_val

    @staticmethod
    def splitter(path):
        # splits the path into a accessible route list
        if path == "/":
            return []
        if path[-1] == "/":
            path = path[:-1]
        return path[1:].split("/")


#    TESTS    #
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # initializes router
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print '404 page not found'
