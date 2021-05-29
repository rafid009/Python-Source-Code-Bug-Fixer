import numpy as np 

def function(x):

	r4 = 6
	u2 = 5
	paths = []
	try:
		if r4 < 7:
			u2 = u2-6
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if r4 <= 5:
			x = x+5
			paths.append(3)
		else:
			r4 = u2-r4
			r4 = 7+r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))