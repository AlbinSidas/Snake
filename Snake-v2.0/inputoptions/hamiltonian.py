class Hamilton():
    """
    https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/
    """

    """
    Måste modifiera den hittade koden befintligt för att det ska fungera och 
    jag ska vara säker på att den söker alla paths, ui nuläget letar den genom en rad
    och returnerar false och därmed också får den inga givna paths.
    """

    def __init__(self, world):
        width = len(world[0])
        height = len(world)
        
        # Kan utgå från denna ovan men kommer behöva göra om den till en 2d graf
        # där ex 0 = 12*12 l'ngd och mot vilka den är länkad
        
        #number_of_nodes = (width)*(height)
        #self.vertices = self.build_vertices(number_of_nodes)
        #self.V = self.build_vertices(number_of_nodes)
        #self.V = width*height- 1
        """
        self.graph = [[0 for column in range(height)]
                         for row in range(width)]
        """
        #self.graph = [[0] * (width - 1) for i in range(height)]
        vertices = width * height - 1
        self.graph = self.build_vertices(vertices)


    def get_action(self, world_list, python, fruit, pygame):
        #path = self.find_path(self.graph, 0, 0)

        path = []
        self.search_graph(0, path)
        print(path)
    """
    def find_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
    """
    """
    Egen implementation:
    Hitta hamiltonian cycle
    i ett system av en undirected cyclic graph

    göra det i !N

    för varje nod jag besöker lägg till att besöka alla barnnoder och generera alla möjliga paths

    Slutmålet är att alla noder ska vara inlkuderade en gång och start och stopp ska vara graph[0] + 12 (alltså under startnoden)
    
    Måste faktiskt inte göra alla permutationer för att hitta alla hamiltoncycler, utan kan stanna efter en har htitats.


    ha alla noder i en lista, för varje steg i listan gå till en granne, (+-12 och +-1)
    
    rekursivt, kolla på första genom index,
    i "barn" är de noder den är connectad till

    kolla om om grannen är slutnoden
        kolla om alla noder finns i pathen
            Klar
        gå till nästa alternativ då den sista noden inte ska besökas förrens sist

    
    
    Kan ej göra det rekursivt eftersom det är för stor statespace.
    
    def search_graph(self, index, curr_path):
        curr_path.append(index)
        connections = self.graph[index]
        for connection in connections:
            if connection == 12:
                temp = curr_path
                temp = temp.sort()
                if temp == list(range(143)):
                    return curr_path
            self.search_graph(connection, curr_path)
    """
    def search_graph(self, indx, curr_path):

        # https://springerplus.springeropen.com/articles/10.1186/s40064-016-2746-8
        # Algorithm 3 är värd att titta på som kan generera paths ser det et ut som

        path = []
        cntr = 0
        indx = 0
        go_to = []
        visited = {}

        while True:
            print(indx)
            if visited.get(indx, None) == None and indx != 12:
                path.append(indx)
                visited[indx] = 1
            else:
                try:
                    indx = go_to.pop()
                except:
                    print(path)
                    #print(len(path))
                    #print(self.graph)
                    #for r in self.graph:
                    #    print(r)
                    exit()
                continue

            # 12 kommer vara den slutgiltiga noden (under längst upp till vänster)
            if indx == 12:
                print(curr_path)
                print("\n\n\nHITTAT 12\n\n\n")
                temp = path
                #temp = temp.sort()
                if temp == list(range(143)):
                    print("HITTAT EN PATH")
                    break
                else:
                    continue

            connections = self.graph[indx]
            go_to += connections
            for connection in connections:
                if connection not in go_to:
                    go_to.append(connection)
            
            indx = go_to.pop()

            cntr += 1
        
        return path

    """
        self.hamCycle()


    ##### SAXAT FRÅN SIDAN 


    ''' Check if this vertex is an adjacent vertex  
        of the previously added vertex and is not  
        included in the path earlier '''
    def isSafe(self, v, pos, path):  
        # Check if current vertex and last vertex  
        # in path are adjacent  
        #print(pos)
        #print(v)
        if self.graph[ path[pos-1] ][v] == 0:  
            return False
  
        # Check if current vertex not already in path  
        for vertex in path:  
            if vertex == v:  
                return False
  
        return True
  
    # A recursive utility function to solve  
    # hamiltonian cycle problem  
    def hamCycleUtil(self, path, pos):  
  
        # base case: if all vertices are  
        # included in the path  
        if pos == self.V:  
            #print("ALLA ÄR UNKLUDERADE")
            # Last vertex must be adjacent to the  
            # first vertex in path to make a cyle  
            if self.graph[ path[pos-1] ][ path[0] ] == 1:  
                return True
            else:  
                return False
  
        # Try different vertices as a next candidate  
        # in Hamiltonian Cycle. We don't try for 0 as  
        # we included 0 as starting point in hamCycle()  
        for v in range(1,self.V):  
  
            if self.isSafe(v, pos, path) == True:  
  
                path[pos] = v  
  
                if self.hamCycleUtil(path, pos+1) == True:  
                    return True
  
                # Remove current vertex if it doesn't
                # lead to a solution
                path[pos] = -1
  
        return False

    def hamCycle(self):  
        #print(self.V)
        path = [-1] * self.V  
        #print(path)
  
        ''' Let us put vertex 0 as the first vertex  
            in the path. If there is a Hamiltonian Cycle,  
            then the path can be started from any point  
            of the cycle as the graph is undirected '''
        path[0] = 0
  
        if self.hamCycleUtil(path,1) == False:  
            print ("Solution does not exist\n") 
            return False
  
        self.printSolution(path)  
        return True

    def printSolution(self, path):  
        print ("Solution Exists: Following", 
                "is one Hamiltonian Cycle") 
        for vertex in path:  
            print (vertex, end = " ") 
        print (path[0], "\n") 

        ####### SAXX

    """

    def build_vertices(self, num_nodes):
        """
        Build a 2D graph where each element in the list is a list
        with information of where the element is connected to.
        [0 0 0 0 0 0 0 0 0 0 0 0]   jag vet  att + 12 framåt kommer vara samma fast rakt nedanför

        Okej:
        + 12 är nedanför
        -1 vänster
        + 1 höger
        - 12 ovanför

        dessa är de enda som är connectade
        """
        graph = {}

        for index in range(num_nodes):
            graph[index] = []
            
            if index + 12 < num_nodes:
                graph[index].append(index + 12)

            # If index - 1 % 12 == 11 then it's reffering to the node from a row above
            if index - 1 >= 0 and (index - 1) % 12 != 11:
                graph[index].append(index - 1)

            # If index - 1 % 12 == 0 then it's reffering to the node from the next row
            if index + 1 < num_nodes and (index + 1) % 12 != 0:
                graph[index].append(index + 1)
            if index - 12 >= 0:
                graph[index].append(index - 12)
        
        return graph
