import numpy as np 

def function(x):

	b6 = 2
	h6 = 8
	paths = []
	try:
		if x > 3:
			b6 = b6/9
			h6 = h6+2
			paths.append(1)
		else:
			h6 = 0/h6
			x = 4*0
			paths.append(2)
		if x <= 3:
			b6 = 1+b6
			x = x-5
			paths.append(3)
		else:
			x = h6-x
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))