import numpy as np 

def function(x):

	g5 = x
	a8 = 9
	x = 3
	paths = []
	try:
		if g5 <= 4:
			x = x-9
			g5 = 3-g5
			paths.append(1)
		else:
			a8 = a8/g5
			x = x+x
			paths.append(2)
		if g5 >= 5:
			x = x-2
			a8 = a8-a8
			a8 = a8+2
			paths.append(3)
		else:
			x = 1+x
			x = 7+x
			a8 = 2/a8
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