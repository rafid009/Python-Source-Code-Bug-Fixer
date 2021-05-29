import numpy as np 

def function(x):

	e2 = x
	r3 = 9
	paths = []
	try:
		if e2 < 1:
			r3 = r3+9
			e2 = e2/9
			x = 6/x
			paths.append(1)
		else:
			r3 = x*4
			x = x+x
			paths.append(2)
		if x < 8:
			r3 = r3/e2
			paths.append(3)
		else:
			x = x*e2
			r3 = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))