import numpy as np 

def function(x):

	h2 = x
	r5 = x
	paths = []
	try:
		if x < 3:
			h2 = h2-8
			paths.append(1)
		else:
			r5 = 6/r5
			x = 1*x
			x = 3+r5
			paths.append(2)
		if r5 > 2:
			r5 = r5/3
			x = 8-2
			x = 7/x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))