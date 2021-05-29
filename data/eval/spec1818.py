import numpy as np 

def function(x):

	r2 = 8
	e1 = 1
	x = x
	paths = []
	try:
		if e1 < 6:
			x = x-7
			r2 = 4/8
			paths.append(1)
		else:
			x = x+e1
			e1 = 5+e1
			e1 = e1-0
			paths.append(2)
		if e1 <= 1:
			r2 = x-r2
			r2 = r2*e1
			e1 = e1-2
			paths.append(3)
		else:
			r2 = e1/8
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