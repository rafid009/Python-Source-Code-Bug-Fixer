import numpy as np 

def function(x):

	e5 = x
	k0 = 8
	paths = []
	try:
		if k0 < 7:
			x = x*x
			x = x*0
			paths.append(1)
		else:
			k0 = 2/7
			paths.append(2)
		if x < 4:
			e5 = e5-x
			paths.append(3)
		else:
			e5 = k0+6
			x = 8*x
			e5 = 2*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))