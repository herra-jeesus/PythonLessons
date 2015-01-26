"""
Ülesanne 14 - Sympy
Juhend: https://courses.cs.ttu.ee/w/images/e/ee/ITI0140_2014_Loeng_sympy1.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

import sympy

def main():
    a, x = sympy.symbols('a x')
  	
    f1 = x**3 + 4*x**2 + 100
    f2 = (7+1)*sympy.sin(x) + sympy.cos(x)

    S = sympy.Abs(sympy.integrate(f2-f1, (x,0,a)))
    
    print(S)
    print(S.subs(a, 20))
    print(S.evalf(subs={a: 20}))

if __name__ == "__main__":
    main()
