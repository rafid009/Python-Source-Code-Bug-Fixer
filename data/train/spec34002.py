import numpy as np 

def function(x):

	j3 = 2
	g3 = 2
	paths = []
	try:
		if j3 <= 9:
			g3 = g3/8
			g3 = g3*2
			j3 = g3-j3
			paths.append(1)
		else:
			j3 = 8+g3
			x = 9-x
			g3 = g3+g3
			paths.append(2)
		if g3 > 5:
			j3 = 4*j3
			j3 = j3+4
			j3 = j3/4
			paths.append(3)
		else:
			j3 = j3+7
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