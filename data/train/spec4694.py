import numpy as np 

def function(x):

	e6 = 8
	h6 = x
	x = x
	paths = []
	try:
		if x <= 6:
			e6 = 1-2
			e6 = e6*9
			h6 = h6/e6
			paths.append(1)
		else:
			x = 6*x
			x = x+6
			x = x/1
			paths.append(2)
		if h6 <= 5:
			x = x+7
			paths.append(3)
		else:
			x = x+h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		e6 = h6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))