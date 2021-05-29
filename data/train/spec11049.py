import numpy as np 

def function(x):

	h1 = 5
	n8 = x
	paths = []
	try:
		if x < 8:
			h1 = x-1
			paths.append(1)
		else:
			n8 = n8/h1
			h1 = n8+9
			x = x/n8
			paths.append(2)
		if n8 < 4:
			x = 8-x
			paths.append(3)
		else:
			x = 1+6
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		n8 = h1**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))