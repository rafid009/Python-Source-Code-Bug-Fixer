import numpy as np 

def function(x):

	g0 = 3
	r0 = x
	paths = []
	try:
		if g0 > 2:
			g0 = 7+r0
			paths.append(1)
		else:
			g0 = 3+g0
			r0 = 5*r0
			g0 = x/3
			paths.append(2)
		if r0 <= 4:
			g0 = g0+9
			paths.append(3)
		else:
			x = 4*g0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))