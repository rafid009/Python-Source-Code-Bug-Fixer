import numpy as np 

def function(x):

	r9 = x
	a0 = x
	paths = []
	try:
		if r9 < 3:
			a0 = 4/7
			paths.append(1)
		else:
			a0 = 2-a0
			r9 = r9/x
			paths.append(2)
		if x > 3:
			a0 = 6/a0
			x = x-3
			paths.append(3)
		else:
			r9 = r9+9
			a0 = r9+x
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		r9 = a0**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))