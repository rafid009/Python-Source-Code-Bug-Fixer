import numpy as np 

def function(x):

	h2 = x
	k7 = x
	paths = []
	try:
		if h2 > 4:
			h2 = 5-h2
			x = x/x
			paths.append(1)
		else:
			k7 = 6*k7
			paths.append(2)
		if h2 > 6:
			k7 = 0+0
			k7 = k7*x
			k7 = k7+h2
			paths.append(3)
		else:
			h2 = h2*9
			h2 = x*h2
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))