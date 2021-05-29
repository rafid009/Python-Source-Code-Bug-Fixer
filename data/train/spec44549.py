import numpy as np 

def function(x):

	h2 = x
	r0 = 2
	paths = []
	try:
		if r0 < 5:
			h2 = h2+x
			h2 = 6+h2
			paths.append(1)
		else:
			h2 = x-h2
			h2 = h2+5
			paths.append(2)
		if x > 7:
			r0 = h2-5
			paths.append(3)
		else:
			x = x+r0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))