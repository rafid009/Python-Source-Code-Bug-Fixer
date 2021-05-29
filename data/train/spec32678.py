import numpy as np 

def function(x):

	h2 = 7
	r1 = 1
	paths = []
	try:
		if x < 5:
			h2 = x/h2
			r1 = 8/9
			x = r1/x
			paths.append(1)
		else:
			r1 = r1+1
			h2 = h2+8
			h2 = r1+9
			paths.append(2)
		if x > 0:
			h2 = h2/1
			paths.append(3)
		else:
			x = h2*x
			r1 = r1-4
			x = h2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))