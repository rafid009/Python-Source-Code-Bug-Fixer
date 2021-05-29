import numpy as np 

def function(x):

	o5 = 4
	h2 = x
	x = 0
	paths = []
	try:
		if x < 1:
			h2 = h2+2
			h2 = o5-8
			paths.append(1)
		else:
			x = 2-x
			o5 = 4-0
			paths.append(2)
		if h2 < 2:
			h2 = 2*6
			h2 = o5-h2
			paths.append(3)
		else:
			o5 = o5/7
			o5 = h2*h2
			x = x*x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		o5 = h2**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))