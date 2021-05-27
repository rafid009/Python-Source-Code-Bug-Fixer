import numpy as np 

def function(x):

	e3 = x
	j3 = x
	paths = []
	try:
		if j3 <= 7:
			j3 = 8*j3
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if x <= 9:
			e3 = 2-6
			e3 = e3*e3
			paths.append(3)
		else:
			x = e3/3
			x = 5+3
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))