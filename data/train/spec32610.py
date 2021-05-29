import numpy as np 

def function(x):

	g3 = 3
	j3 = x
	paths = []
	try:
		if j3 < 5:
			j3 = g3/j3
			j3 = j3*0
			paths.append(1)
		else:
			g3 = g3-1
			paths.append(2)
		if x <= 6:
			g3 = 8+g3
			j3 = j3-j3
			j3 = 2*g3
			paths.append(3)
		else:
			g3 = g3/8
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