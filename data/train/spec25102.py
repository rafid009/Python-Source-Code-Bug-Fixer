import numpy as np 

def function(x):

	e6 = 8
	r3 = 4
	x = x
	paths = []
	try:
		if r3 <= 7:
			r3 = 1+6
			paths.append(1)
		else:
			x = x*e6
			paths.append(2)
		if r3 > 1:
			e6 = e6+5
			paths.append(3)
		else:
			r3 = r3+e6
			r3 = r3+8
			x = e6*1
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