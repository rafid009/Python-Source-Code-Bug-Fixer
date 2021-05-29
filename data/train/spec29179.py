import numpy as np 

def function(x):

	v7 = x
	w4 = 9
	paths = []
	try:
		if x >= 5:
			w4 = w4/w4
			paths.append(1)
		else:
			w4 = w4/7
			paths.append(2)
		if v7 <= 5:
			x = x-w4
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))