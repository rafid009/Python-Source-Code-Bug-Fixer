import numpy as np 

def function(x):

	g4 = 2
	v3 = x
	paths = []
	try:
		if v3 >= 9:
			v3 = v3-6
			g4 = 7*x
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if x < 7:
			x = 3/x
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))