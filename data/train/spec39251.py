import numpy as np 

def function(x):

	f3 = x
	v7 = x
	paths = []
	try:
		if v7 < 0:
			f3 = 0*f3
			f3 = f3*f3
			paths.append(1)
		else:
			f3 = x*4
			paths.append(2)
		if v7 > 4:
			v7 = v7/4
			f3 = 1+f3
			f3 = x+f3
			paths.append(3)
		else:
			x = x+v7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))