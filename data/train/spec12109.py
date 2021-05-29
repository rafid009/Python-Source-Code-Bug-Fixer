import numpy as np 

def function(x):

	a6 = 5
	g5 = x
	paths = []
	try:
		if x < 8:
			g5 = x-9
			x = x-0
			paths.append(1)
		else:
			g5 = 1-g5
			paths.append(2)
		if a6 <= 7:
			x = x/4
			x = a6+g5
			paths.append(3)
		else:
			g5 = x/2
			x = g5-2
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