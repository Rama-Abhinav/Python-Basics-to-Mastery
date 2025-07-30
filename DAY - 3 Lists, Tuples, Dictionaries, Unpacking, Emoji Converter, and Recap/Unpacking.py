# Exploring the feature of unpacking

List = [1,2,3]
Tuple = (1,2,3,4,5)

a,b,c,= List

## Extended Unpacking 
*e,f,g = Tuple

h,*i,j = Tuple

u,o,*p = Tuple

print(f"a={a}, b={b}, c={c}" )

print(f"e={e}, f={f}, g={g}" )

print(f"h={h}, i={i}, j={j}" )

print(f"u={u}, o={o}, p={p}" )

