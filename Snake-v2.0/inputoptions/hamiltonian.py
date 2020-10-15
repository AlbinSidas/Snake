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

        #self.graph = [[0] * (breadth - 1) for i in range(height)]
        # Kan utgå från denna ovan men kommer behöva göra om den till en 2d graf
        # där ex 0 = 12*12 l'ngd och mot vilka den är länkad
        
        number_of_nodes = (width)*(height)
        #self.vertices = self.build_vertices(number_of_nodes)
        #self.V = self.build_vertices(number_of_nodes)
        self.V = width*height- 1
        self.graph = [[0 for column in range(height)]
                         for row in range(width)]



    def get_action(self, world_list, python, fruit, pygame):
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
        graph = []

        for index in range(num_nodes):
            connections = [0] * num_nodes
            
            if index + 12 < num_nodes:
                connections[index + 12] = 1
            if index - 1 > 0:
                connections[index - 1] = 1
            if index + 1 < num_nodes:
                connections[index + 1] = 1
            if index - 12 > 0:
                connections[index - 12] = 1
            graph.append(connections)
        
        return graph
