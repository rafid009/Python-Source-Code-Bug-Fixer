import numpy as np 

def function(x):

	r1 = 6
	e0 = x
	paths = []
	try:
		if e0 > 8:
			e0 = 9+e0
			paths.append(1)
		else:
			e0 = e0+8
			r1 = r1+r1
			x = x/7
			paths.append(2)
		if x > 1:
			x = r1*0
			e0 = e0*e0
			paths.append(3)
		else:
			e0 = e0/4
			r1 = e0/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))