import numpy as np 

def function(x):

	r2 = x
	a1 = x
	paths = []
	try:
		if x < 6:
			r2 = r2-2
			paths.append(1)
		else:
			r2 = r2/x
			paths.append(2)
		if x > 9:
			a1 = a1-1
			r2 = 2*x
			x = x*a1
			paths.append(3)
		else:
			x = 8+x
			a1 = 0-5
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		a1 = r2**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))