import numpy as np 

def function(x):

	i4 = 1
	g3 = 5
	paths = []
	try:
		if g3 < 5:
			g3 = g3*g3
			x = 7/x
			i4 = i4+4
			paths.append(1)
		else:
			i4 = i4+x
			i4 = 1*3
			i4 = 2*i4
			paths.append(2)
		if x <= 8:
			x = 5+x
			paths.append(3)
		else:
			i4 = 8/1
			x = 1*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))