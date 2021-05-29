import numpy as np 

def function(x):

	n8 = x
	h3 = x
	paths = []
	try:
		if h3 <= 4:
			h3 = x-4
			h3 = 1*n8
			paths.append(1)
		else:
			h3 = 6/2
			h3 = h3/4
			paths.append(2)
		if x > 5:
			x = x*1
			paths.append(3)
		else:
			n8 = n8+4
			h3 = 7+h3
			n8 = n8*6
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))