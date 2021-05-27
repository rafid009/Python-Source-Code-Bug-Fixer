import numpy as np 

def function(x):

	r1 = 8
	h1 = 1
	paths = []
	try:
		if x <= 7:
			x = 5*1
			x = x-9
			h1 = h1-8
			paths.append(1)
		else:
			r1 = 2/r1
			x = 7/x
			paths.append(2)
		if x <= 8:
			r1 = 8/r1
			r1 = h1*r1
			r1 = r1*5
			paths.append(3)
		else:
			r1 = r1*0
			h1 = 9-h1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))