import numpy as np 

def function(x):

	v5 = 6
	e0 = 1
	paths = []
	try:
		if x > 7:
			e0 = e0*1
			x = v5*x
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if v5 > 1:
			v5 = 7/e0
			x = 1*x
			v5 = 5+e0
			paths.append(3)
		else:
			e0 = 0+e0
			v5 = v5+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))