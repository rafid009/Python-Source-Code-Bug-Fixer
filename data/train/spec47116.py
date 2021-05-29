import numpy as np 

def function(x):

	y7 = 5
	w7 = x
	paths = []
	try:
		if w7 < 4:
			w7 = w7/w7
			y7 = 4+w7
			paths.append(1)
		else:
			y7 = y7+3
			paths.append(2)
		if x >= 3:
			x = x+9
			y7 = 5/w7
			paths.append(3)
		else:
			y7 = 8+7
			y7 = y7*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))