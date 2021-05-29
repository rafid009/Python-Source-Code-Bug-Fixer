import numpy as np 

def function(x):

	a9 = 9
	r2 = 1
	paths = []
	try:
		if a9 >= 6:
			x = x/8
			r2 = x+r2
			a9 = a9-4
			paths.append(1)
		else:
			r2 = a9*r2
			paths.append(2)
		if a9 <= 9:
			r2 = 0-r2
			paths.append(3)
		else:
			x = a9*5
			r2 = r2*2
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))