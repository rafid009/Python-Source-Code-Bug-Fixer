import numpy as np 

def function(x):

	h4 = 6
	a6 = 2
	x = x
	paths = []
	try:
		if h4 >= 2:
			a6 = a6*8
			h4 = x+h4
			paths.append(1)
		else:
			a6 = 6*a6
			x = x+x
			paths.append(2)
		if x < 8:
			h4 = h4*7
			a6 = a6+h4
			paths.append(3)
		else:
			a6 = a6+1
			h4 = 5-7
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))