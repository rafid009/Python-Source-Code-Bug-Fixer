import numpy as np 

def function(x):

	f8 = 5
	v5 = 0
	paths = []
	try:
		if f8 >= 0:
			f8 = 3/f8
			paths.append(1)
		else:
			v5 = 1*v5
			v5 = 3/v5
			f8 = x*f8
			paths.append(2)
		if v5 > 2:
			x = x-3
			f8 = x-9
			v5 = v5/9
			paths.append(3)
		else:
			f8 = f8*x
			f8 = 4*5
			v5 = v5+v5
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