import numpy as np 

def function(x):

	h6 = x
	n4 = x
	paths = []
	try:
		if h6 > 3:
			x = x-1
			paths.append(1)
		else:
			n4 = n4*0
			n4 = n4*5
			paths.append(2)
		if x > 5:
			x = x-2
			paths.append(3)
		else:
			x = x+5
			h6 = 5*h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))