import numpy as np 

def function(x):

	f1 = x
	g5 = 8
	paths = []
	try:
		if x > 5:
			x = x+g5
			g5 = g5+g5
			paths.append(1)
		else:
			x = 1/g5
			g5 = g5/5
			paths.append(2)
		if g5 > 2:
			x = 6*x
			g5 = 0-g5
			x = x/f1
			paths.append(3)
		else:
			f1 = 8+f1
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