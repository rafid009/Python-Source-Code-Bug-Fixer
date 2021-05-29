import numpy as np 

def function(x):

	h8 = 4
	n8 = 1
	paths = []
	try:
		if n8 > 4:
			x = 8/h8
			paths.append(1)
		else:
			h8 = h8/7
			paths.append(2)
		if n8 < 2:
			h8 = x/h8
			x = x+4
			x = 3*8
			paths.append(3)
		else:
			h8 = h8/3
			n8 = n8-8
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		n8 = h8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))