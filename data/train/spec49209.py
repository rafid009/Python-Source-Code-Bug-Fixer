import numpy as np 

def function(x):

	l9 = 9
	h4 = x
	paths = []
	try:
		if l9 <= 0:
			h4 = h4+h4
			h4 = h4/2
			x = x+x
			paths.append(1)
		else:
			l9 = h4*l9
			h4 = 8*h4
			paths.append(2)
		if x < 8:
			h4 = h4-2
			h4 = h4+l9
			paths.append(3)
		else:
			l9 = l9+x
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