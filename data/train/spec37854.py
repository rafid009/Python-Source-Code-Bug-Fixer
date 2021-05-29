import numpy as np 

def function(x):

	l3 = 3
	r2 = x
	x = x
	paths = []
	try:
		if l3 > 7:
			r2 = 7-r2
			paths.append(1)
		else:
			l3 = 9/l3
			x = x-9
			x = 1/x
			paths.append(2)
		if r2 <= 7:
			x = 2+x
			paths.append(3)
		else:
			r2 = r2*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))