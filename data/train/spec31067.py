import numpy as np 

def function(x):

	a4 = 8
	h4 = 5
	paths = []
	try:
		if a4 >= 1:
			h4 = 7+1
			paths.append(1)
		else:
			a4 = h4/a4
			x = x-5
			a4 = a4-3
			paths.append(2)
		if x <= 5:
			h4 = x+2
			a4 = 6*x
			x = a4/1
			paths.append(3)
		else:
			h4 = 8+h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		a4 = h4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))