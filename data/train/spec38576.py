import numpy as np 

def function(x):

	g1 = 5
	j5 = x
	x = x
	paths = []
	try:
		if x < 7:
			g1 = 9-g1
			g1 = j5-g1
			paths.append(1)
		else:
			x = j5-8
			paths.append(2)
		if j5 <= 7:
			x = 3+j5
			paths.append(3)
		else:
			j5 = g1+j5
			g1 = 1/g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))