

def gen_node(node, children):
    if not isinstance(children, list):
        children = [children]
    return {"node": node, "children": children}


def ConvertJsAst(node):
    """
    Convert Original JavaScript AST into Json, whose nodes only have 'node' and 'children' members.
    """
    if isinstance(node, str):
        return None
    
    elif isinstance(node, list):
        return [ConvertJsAst(x) for x in node if x is not None]

    elif isinstance(node, dict):
        if "type" not in node:
            return None

        if node['type'] == "Identifier":
            children = [gen_node(node['name'], list())]

        elif node["type"] == "ExpressionStatement":
            if "directive" in node:
                children = [gen_node(node['directive'], list())]
            else:
                children = [ConvertJsAst(node['expression'])]

        elif node['type'] == "VariableDeclarator":
            children = [ConvertJsAst(node['id']), ConvertJsAst(node['init'])]

        elif node['type'] == "Literal":
            children = [gen_node(node['raw'], list())]

        elif node['type'] in ["BinaryExpression", "AssignmentExpression", "LogicalExpression"]:
            children = [gen_node(node['operator'], [ConvertJsAst(node['left']), ConvertJsAst(node['right'])])]

        elif node['type'] in ["UnaryExpression", "UpdateExpression"]:
            children = [gen_node(node['operator'], [ConvertJsAst(node['argument'])])]

        elif node['type'] in ['MemberExpression']:
            children = [gen_node(".", [ConvertJsAst(node['object']), ConvertJsAst(node['property'])])]

        elif node['type'] in ["CallExpression", "NewExpression"]:
            callee_child = gen_node("callee", ConvertJsAst(node['callee']))
            arguments_child = gen_node("arguments", ConvertJsAst(node['arguments']))
            children = [callee_child, arguments_child]

        elif node['type'] == "FunctionDeclaration":
            id_child = gen_node("func_name", ConvertJsAst(node['id']))
            params_child = gen_node("func_params", ConvertJsAst(node['params']))
            body_child = gen_node("body", ConvertJsAst(node['body']))
            children = [id_child, params_child, body_child]

        else:
            tmp = [ConvertJsAst(val) for key, val in node.items() if key not in ['range', 'type']]
            children = list()
            for x in tmp:
                if isinstance(x, list):
                    children.extend(x)
                else:
                    children.append(x)

        children = [child for child in children if child is not None]
        return gen_node(node['type'], children)


def DFS_traverse(root):
    node_stack = [(root, 0)]
    
    while node_stack:
        node, depth = node_stack.pop(-1)
        for i in range(len(node['children']) - 1, -1, -1):
            node_stack.append((node['children'][i], depth + 1))
        print("\t" * depth + "└ " + node["node"])
