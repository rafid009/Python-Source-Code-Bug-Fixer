import numpy as np 

def function(x):

	g4 = x
	r0 = 0
	paths = []
	try:
		if g4 >= 3:
			g4 = g4*0
			paths.append(1)
		else:
			r0 = r0+g4
			x = 2*x
			g4 = r0*g4
			paths.append(2)
		if g4 >= 1:
			x = 1+x
			paths.append(3)
		else:
			r0 = 9+5
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))