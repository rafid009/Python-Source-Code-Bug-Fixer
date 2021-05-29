import numpy as np 

def function(x):

	r1 = x
	e9 = x
	paths = []
	try:
		if r1 > 0:
			x = x*x
			r1 = r1*r1
			e9 = e9+x
			paths.append(1)
		else:
			x = 6+5
			x = x+5
			e9 = e9+e9
			paths.append(2)
		if r1 < 9:
			x = r1-7
			x = x+0
			paths.append(3)
		else:
			r1 = 4/e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))