import numpy as np 

def function(x):

	h7 = x
	l0 = 9
	paths = []
	try:
		if l0 > 3:
			x = h7+x
			h7 = 7+5
			l0 = 3-l0
			paths.append(1)
		else:
			x = 8-x
			l0 = 5*l0
			h7 = 5-6
			paths.append(2)
		if l0 < 8:
			h7 = l0+5
			paths.append(3)
		else:
			h7 = l0/h7
			h7 = l0/l0
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		h7 = l0**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))