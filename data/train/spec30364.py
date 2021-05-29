import numpy as np 

def function(x):

	h2 = x
	a2 = x
	paths = []
	try:
		if x < 8:
			h2 = a2-h2
			paths.append(1)
		else:
			x = 6/x
			x = x/4
			x = x-8
			paths.append(2)
		if h2 > 2:
			x = 7*x
			a2 = 4+a2
			paths.append(3)
		else:
			a2 = a2+7
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		h2 = a2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))