import numpy as np 

def function(x):

	b2 = 7
	h4 = x
	paths = []
	try:
		if h4 <= 9:
			h4 = h4*x
			x = 7+x
			h4 = h4-8
			paths.append(1)
		else:
			x = x*h4
			x = 3-b2
			x = x+b2
			paths.append(2)
		if b2 >= 3:
			b2 = 9/b2
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))