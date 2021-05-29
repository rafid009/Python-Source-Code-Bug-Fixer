import numpy as np 

def function(x):

	h4 = x
	b2 = x
	paths = []
	try:
		if h4 < 0:
			x = 6-x
			h4 = h4*6
			b2 = b2*0
			paths.append(1)
		else:
			b2 = b2-5
			paths.append(2)
		if b2 >= 6:
			h4 = h4/5
			b2 = b2/9
			b2 = h4/5
			paths.append(3)
		else:
			b2 = 9*b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))