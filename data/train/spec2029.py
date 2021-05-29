import numpy as np 

def function(x):

	p3 = x
	h8 = x
	paths = []
	try:
		if h8 > 5:
			p3 = p3*5
			h8 = h8/2
			p3 = p3/6
			paths.append(1)
		else:
			h8 = h8-6
			x = 1/p3
			paths.append(2)
		if h8 > 4:
			p3 = 6+p3
			paths.append(3)
		else:
			x = 7/2
			x = x+1
			x = x+4
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))