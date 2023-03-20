class Searching:
    def breadfirstsearch(self,graph,initial,goal):
        """
        Metode search dengan bread first search.
        parameter graph  dan tujuan
        """
        
        queue = [initial]
        expand_node = [initial]
        track = [initial]
        parent = [i for i in graph.keys()]
        while len(queue) > 0:
            node = queue.pop(0)
            if node ==goal:
                return track
            
            if node in parent:
                for neighbour in graph[node]:
                    if neighbour not in expand_node:
                        queue.append(neighbour)
                        expand_node.append(neighbour)
                        track.append(neighbour)



                
                
            





