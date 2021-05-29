import numpy as np 

def function(x):

	g5 = 7
	v3 = 7
	paths = []
	try:
		if x >= 0:
			v3 = g5+6
			g5 = x-1
			v3 = x+g5
			paths.append(1)
		else:
			g5 = x/6
			x = x-6
			v3 = 9-v3
			paths.append(2)
		if g5 > 9:
			x = 5*x
			v3 = v3-3
			g5 = 3/g5
			paths.append(3)
		else:
			v3 = v3/x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))