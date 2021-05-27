import numpy as np 

def function(x):

	i0 = x
	g3 = 2
	paths = []
	try:
		if g3 >= 5:
			x = x/x
			i0 = 3*x
			paths.append(1)
		else:
			i0 = i0*g3
			g3 = g3+g3
			i0 = i0+g3
			paths.append(2)
		if g3 > 2:
			g3 = g3-4
			g3 = g3*1
			g3 = x+6
			paths.append(3)
		else:
			g3 = g3*5
			i0 = x*i0
			i0 = i0/9
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))