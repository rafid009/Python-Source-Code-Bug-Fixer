import numpy as np 

def function(x):

	r6 = x
	a9 = 8
	paths = []
	try:
		if r6 >= 6:
			r6 = 3+5
			r6 = 2/3
			paths.append(1)
		else:
			r6 = x*3
			x = 4+x
			paths.append(2)
		if r6 > 0:
			r6 = r6-3
			paths.append(3)
		else:
			x = 6+x
			r6 = 4+r6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))