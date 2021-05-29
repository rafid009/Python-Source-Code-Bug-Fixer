import numpy as np 

def function(x):

	x7 = 7
	g5 = x
	paths = []
	try:
		if x7 <= 5:
			x7 = 7+x7
			x7 = x7*8
			paths.append(1)
		else:
			x = x-x7
			paths.append(2)
		if x >= 8:
			x = 7-x
			x7 = 1+9
			x7 = x7+g5
			paths.append(3)
		else:
			g5 = 4/g5
			x = g5*x
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