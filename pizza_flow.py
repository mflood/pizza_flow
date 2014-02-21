class Node(object):

    def __init__(self, name):
        self.name = name
        self.outgoing_edges = []
        self.incoming_edges = []

class Edge(object):

    def __init__(self, source_node, target_node, capacity):   
        self.source_node = source_node
        self.target_node = target_node
        self.capacity = capacity
        self.usage = 0
        self.source_node.outgoing_edges.append(self) 
        self.target_node.incoming_edges.append(self) 
        self.outgoing_color = "white"
        self.incoming_color = "white"

    def get_forward_availability(self):
        return self.capacity - self.usage

    def get_reverse_capacity(self):
        return self.usage

    def __repr__(self):
        ret = ""
        ret = "%s->%s (%s/%s) %s %s" % (
            self.source_node.name,
            self.target_node.name,
            self.usage,
            self.capacity,
            self.outgoing_color,
            self.incoming_color
        )
        return ret

class Bipartite(object):

    def __init__(self):

        self._start_node = Node("START")
        self._end_node = Node("END")

        self._left_nodes = []
        self._right_nodes = []

        self._edges = []

    def __repr__(self):
        ret = ""
        for edge in self._edges:
            ret += "%s\n" % edge
        return ret

    def add_left_node(self, node_name, capacity=1):
        new_node = Node(node_name)
        self._left_nodes.append(new_node)
        e = Edge(self._start_node, new_node, capacity)
        self._edges.append(e)

    def add_right_node(self, node_name, capacity=1):
        new_node = Node(node_name)
        self._right_nodes.append(new_node)
        e = Edge(new_node, self._end_node, capacity)
        self._edges.append(e)

    def find_left_node_by_name(self, node_name):
        for node in self._left_nodes:
            if node.name == node_name:
                return node

    def find_right_node_by_name(self, node_name):
        for node in self._right_nodes:
            if node.name == node_name:
                return node

    def link(self, left_node, right_node, capacity=1):
        left = self.find_left_node_by_name(left_node) 
        right = self.find_right_node_by_name(right_node) 
        e = Edge(left, right, capacity)
        self._edges.append(e)

    def color_edges_white(self):
        for edge in self._edges:
            edge.outgoing_color = "white"
            edge.incoming_color = "white"

    def solve(self):
        while self.find_path():
            pass
        

        print "--- people and what they should eat ---"
        for node in self._left_nodes:
            for e in node.outgoing_edges:
                if e.usage:
                    print e


        print "--- number of slices from each pizza that will be consumed ---"
        for node in self._right_nodes:
            total = 0    
            for e in node.outgoing_edges:
                total += e.usage
            print "%s: %s" % (node.name, total)


    def find_path(self):
        self.color_edges_white()
        path_edges = []
        current_node = self._start_node
        if not self.visit(self._start_node):
            return False

        for e in self._edges:
            if e.outgoing_color == "YAY":
                e.usage += 1
            if e.incoming_color == "YAY":
                e.usage -= 1
        return True

    def visit(self, node):
        if node == self._end_node:
            return True
        for edge in node.outgoing_edges:
            if edge.outgoing_color == "white":
                if edge.get_forward_availability():
                    edge.outgoing_color = "grey"
                    if self.visit(edge.target_node):
                        edge.outgoing_color="YAY"
                        return True
                else:
                    edge.outgoing_color='black'

        for edge in node.incoming_edges:
            if edge.incoming_color == "white":
                if edge.get_reverse_capacity():
                    edge.incoming_color = "grey"
                    if self.visit(edge.source_node):
                        edge.incoming_color="YAY"
                        return True
                else:
                    edge.incoming_color='black'
        return False


b = Bipartite()

# add people who are eating and the maximum number of slices they
# anticipate eating
b.add_left_node("Flood", 3)
b.add_left_node("Craig", 3)
b.add_left_node("Tavis", 4)
b.add_left_node("Oz", 4)
b.add_left_node("Marc", 3)
b.add_left_node("Mike", 3)
b.add_left_node("Tinkler", 3)

# second argument is number of slices each
# pizza provides.  St to 0 to turn off a pizza
# if you buy more than one pizza of the same type, 
# just double the number of slices

b.add_right_node("Sausage", 0)
b.add_right_node("Pepperoni", 8)
b.add_right_node("Vegetarian", 8)
b.add_right_node("Meat Lovers", 0)
b.add_right_node("Mushroom", 8)


# Link people to pizzas by specifiying
# the number of slices they would be willing to eat of that
# particular pizza if they had to.
b.link("Flood", "Pepperoni", 1)
b.link("Flood", "Sausage", 1)
b.link("Flood", "Meat Lovers", 1)
b.link("Flood", "Vegetarian", 1)

b.link("Craig", "Vegetarian", 3)
b.link("Craig", "Mushroom", 3)
b.link("Tinkler", "Mushroom", 3)

b.link("Oz", "Pepperoni", 4)
b.link("Oz", "Meat Lovers", 4)

b.solve()

# if you want to see the graph in its final state, print it:
# print
# print b
