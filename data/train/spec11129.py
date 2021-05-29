import numpy as np 

def function(x):

	w7 = x
	e8 = x
	paths = []
	try:
		if w7 < 8:
			e8 = e8-1
			paths.append(1)
		else:
			x = 3*9
			e8 = 7-w7
			paths.append(2)
		if e8 <= 9:
			e8 = e8-1
			x = x+x
			w7 = w7-3
			paths.append(3)
		else:
			e8 = 6+7
			w7 = 4-w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))