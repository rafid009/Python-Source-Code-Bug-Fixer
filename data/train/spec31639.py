import numpy as np 

def function(x):

	a8 = x
	h2 = x
	paths = []
	try:
		if h2 > 3:
			x = x/h2
			a8 = 4-5
			paths.append(1)
		else:
			a8 = 0+h2
			paths.append(2)
		if x > 6:
			h2 = h2-4
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))