def is_variable(x):
    """Returns True if x is a variable (represented as a lowercase string)."""
    return isinstance(x, str) and x.islower()

def is_constant(x):
    """Returns True if x is a constant (represented as an uppercase string)."""
    return isinstance(x, str) and x.isupper()

def occurs_check(var, expr):
    """Returns True if the variable occurs inside the given expression."""
    if var == expr:
        return True
    if isinstance(expr, list):
        return any(occurs_check(var, sub_expr) for sub_expr in expr)
    return False

def apply_substitution(subst, expr):
    """Applies a substitution set (dictionary) to an expression recursively."""
    if not subst:
        return expr
    if isinstance(expr, str):
        return subst.get(expr, expr)
    if isinstance(expr, list):
        return [apply_substitution(subst, item) for item in expr]
    return expr

def unify(psi1, psi2):
   
    if isinstance(psi1, str) or isinstance(psi2, str):
       
        if psi1 == psi2:
            return {}
       
       
        elif is_variable(psi1):
         
            if occurs_check(psi1, psi2):
                return "FAILURE"
           
            else:
                return {psi1: psi2}
       
        elif is_variable(psi2):
            if occurs_check(psi2, psi1):
                return "FAILURE"
            else:
                return {psi2: psi1}
       
        else:
            return "FAILURE"

    if psi1[0] != psi2[0]:
        return "FAILURE"

    if len(psi1) != len(psi2):
        return "FAILURE"

    subst = {}

    for i in range(1, len(psi1)):
        s = unify(psi1[i], psi2[i])
       
        if s == "FAILURE":
            return "FAILURE"
       
        if s:
            psi1 = apply_substitution(s, psi1)
            psi2 = apply_substitution(s, psi2)
           
            new_subst = {k: apply_substitution(s, v) for k, v in subst.items()}
            new_subst.update(s)
            subst = new_subst

    return subst

if __name__ == "__main__":
    expr1 = ["P", "x", "A"]
    expr2 = ["P", "B", "y"]
    print("Unifying P(x, A) and P(B, y):", unify(expr1, expr2))

    expr3 = ["P", "x", "x"]
    expr4 = ["P", "A", "B"]
    print("Unifying P(x, x) and P(A, B):", unify(expr3, expr4))
    expr5 = ["P", "x"]
    expr6 = ["P", ["f", "x"]]
    print("Unifying P(x) and P(f(x)):", unify(expr5, expr6))

    expr7=["ABCD"]
    expr8=["ABCD"]
    print("Unifying 7 and 8:", unify(expr7, expr8))

    expr3 = ["X", "M(X)"]
    expr4 = ["John", "X"]
    print("Unifying 3 and 4:", unify(expr3, expr4))