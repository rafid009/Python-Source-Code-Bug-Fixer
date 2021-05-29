import numpy as np 

def function(x):

	h4 = x
	b5 = x
	x = 2
	paths = []
	try:
		if b5 >= 1:
			b5 = b5*x
			paths.append(1)
		else:
			x = 0/x
			b5 = 0+6
			paths.append(2)
		if h4 < 4:
			x = 5*2
			paths.append(3)
		else:
			x = x/9
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