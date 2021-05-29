import numpy as np 

def function(x):

	l5 = 6
	h2 = x
	paths = []
	try:
		if x > 3:
			x = 6+0
			l5 = l5+x
			x = 8-x
			paths.append(1)
		else:
			h2 = l5*l5
			h2 = l5/l5
			paths.append(2)
		if l5 <= 3:
			h2 = h2-2
			h2 = h2+3
			paths.append(3)
		else:
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))