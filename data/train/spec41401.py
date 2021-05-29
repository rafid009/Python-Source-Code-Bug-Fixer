import numpy as np 

def function(x):

	h4 = x
	j7 = 2
	paths = []
	try:
		if j7 > 6:
			j7 = x+x
			j7 = j7*2
			paths.append(1)
		else:
			j7 = 3-8
			x = 3*h4
			paths.append(2)
		if x <= 9:
			x = x+0
			paths.append(3)
		else:
			h4 = h4-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))