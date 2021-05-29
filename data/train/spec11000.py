import numpy as np 

def function(x):

	h3 = 2
	n7 = 4
	paths = []
	try:
		if n7 <= 8:
			n7 = n7+9
			h3 = 7/1
			paths.append(1)
		else:
			x = x+5
			n7 = n7-8
			paths.append(2)
		if n7 <= 9:
			h3 = n7*4
			paths.append(3)
		else:
			x = x/h3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))