import numpy as np 

def function(x):

	r8 = 5
	h2 = 0
	paths = []
	try:
		if x >= 2:
			x = 0*x
			h2 = h2/6
			h2 = x*0
			paths.append(1)
		else:
			h2 = h2/5
			x = x-r8
			x = x/1
			paths.append(2)
		if x >= 4:
			h2 = 4+h2
			paths.append(3)
		else:
			x = x-h2
			h2 = h2+2
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