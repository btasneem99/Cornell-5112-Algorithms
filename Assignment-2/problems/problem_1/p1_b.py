# Problem 1b


def maxsum_tree(vertices, adjacency) -> int:
    def find_root(adj):
        parents = {}    
        for node in adj:
            for child in adj[node]:
                parents[child] = node    
        for node in adj:
            if node not in parents:
                return node
        return None

    def get_c_nodes(root):
        children = adjacency[root]
        # print("get_c_nodes of root {} is children {} with length of {}".format(root, children, len(children)))
        if(len(children) != 0):
            # print("len of children is not zero")
            if(len(children)==1):
                # print("len of children is 1")
                left_c_node = children[0]
                right_c_node = None
                # print("for root{}, left_c_node is {} and right_c_node is {}".format(root, left_c_node, right_c_node))
            elif(len(children)==2):
                # print("len of children is 1")
                left_c_node = min(children[0], children[1])
                right_c_node = max(children[0], children[1])
                # print("for root{}, left_c_node is {} and right_c_node is {}".format(root, left_c_node, right_c_node))
        else:
            left_c_node = None
            right_c_node = None
            # print("len of children is 0, and left and right c nodes of root{} are {} and {}".format(root, left_c_node, right_c_node))
        return left_c_node, right_c_node

    global umap
    umap = {}

    def maxSum(root):
        # print("calculating the maxsum of root {}".format(root))
        # base case
        if (root == None):
            # print("root is none, returned 0")
            return 0 
        
        # if the max sum from the node is already in map,return the value
        if (root in umap):
            # print("root is already in umap, returned {}".format(umap[root]))
            return umap[root] 
        
        # if the current node(root) is included in result then find maximum sum
        inc = vertices[root] 
        # print("considering the case when the current node is included in the max: cur node val is {}".format(inc))

        (cur_left_cnode, cur_right_cnode) = get_c_nodes(root)
        # print("children of current node {} are left: {} and right {}".format(root, cur_left_cnode, cur_right_cnode))
        
        # if left of node exists, add their grandchildren
        if(cur_left_cnode != None):
            (cur_left_gcnode_left, cur_left_gcnode_right) = get_c_nodes(cur_left_cnode)
            inc += maxSum(cur_left_gcnode_left) + maxSum(cur_left_gcnode_right)
            # print("left child of root {} exists, left grandchildren are left {} and right {}".format(root, cur_left_gcnode_left, cur_left_gcnode_right))
        # else:
        #     print("no left child for root {}".format(root))

        # if right of node exist,add their grandchildren
        if(cur_right_cnode != None):
            (cur_right_gcnode_left, cur_right_gcnode_right) = get_c_nodes(cur_right_cnode)
            inc += maxSum(cur_right_gcnode_left) + maxSum(cur_right_gcnode_right)
        #     print("right child of root {} exists, left grandchildren are left {} and right {}".format(root, cur_left_gcnode_left, cur_left_gcnode_right))
        # else:
        #     print("no right child for root {}".format(root))

        # if the current node(root) is excluded, find the maximum sum
        # print("considering the case when current node is excluded, so calculating maxsum for the child nodes")
        ex = maxSum(cur_left_cnode) + maxSum(cur_right_cnode)
        
        # store the maximum of including & excluding the node in map
        umap[root] = max(inc, ex)
        # print("inc is {}, ex is {}, umap[root] is assigned {}".format(inc, ex, umap[root]))
        return max(inc, ex) 
    
    tree_root = find_root(adjacency)
    # print("root: {}".format(tree_root))
    # print("maxSum: {}".format(maxSum(tree_root)))
    return maxSum(tree_root)
