import numpy as np 

def function(x):

	u4 = 4
	w7 = 2
	paths = []
	try:
		if x <= 2:
			u4 = 1+u4
			paths.append(1)
		else:
			x = x+9
			u4 = 1/u4
			paths.append(2)
		if u4 >= 2:
			w7 = w7/6
			w7 = 8+u4
			paths.append(3)
		else:
			x = x/x
			u4 = u4+x
			u4 = 2-u4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))