import numpy as np 

def function(x):

	r2 = x
	h1 = x
	paths = []
	try:
		if r2 < 6:
			x = x/h1
			r2 = h1*5
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x > 7:
			r2 = 7+5
			r2 = 5/r2
			x = x*6
			paths.append(3)
		else:
			r2 = h1*h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		r2 = h1**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))