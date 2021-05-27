import numpy as np 

def function(x):

	b5 = x
	h4 = x
	paths = []
	try:
		if h4 >= 4:
			x = x-5
			h4 = h4-1
			paths.append(1)
		else:
			h4 = 6/h4
			x = x*4
			b5 = b5/4
			paths.append(2)
		if b5 > 7:
			x = 3-h4
			x = 2+x
			h4 = 6*h4
			paths.append(3)
		else:
			h4 = h4*2
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))