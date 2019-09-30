"""
A Demo to test convert function.
"""
# coding=utf-8
import js2py
import json
from convert import ConvertJsAst, DFS_traverse

def demo(): 

    esprima = js2py.require("esprima")

    with open("./data/sample.js", "r") as fin:
        js_code = fin.read()
    
    js_ast_origin = esprima.parse(js_code).to_dict()
    
    js_ast_modified = ConvertJsAst(js_ast_origin)

    print(json.dumps(js_ast_origin, indent=4))

    print("-" * 128)
    
    print(json.dumps(js_ast_modified, indent=4))

    print("-" * 128)
    DFS_traverse(js_ast_modified)

demo()