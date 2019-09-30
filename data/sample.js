// ExpressionStatement
"use strict;"

// VariableDeclaration
var a = 1;

// FunctionDeclaration
function add(d) {
    return a + d;
}

// CallExpression & BinaryExpression
var c = add(2) + b;

// ObjectExpression
var x = {'key': true};

// MemberExpression
x.key;

// UnaryExpression & IfStatement
if (!x.key) {
    a = 0;
}else{
    a = 1;
}

// ForStatement & UpdateExpression
for (var i=0; i<5; i++) {
    a = a + 1;
}

// SwitchStatement & SwitchCase
switch(a) {
    case 0: c=0;
    case 1: c=1;
    case 2: c=2;
}

// TryStatement & CatchClause
try {
    foo();
} catch(e) {
    console.error(e);
} finally {
    console.log("success");
}
