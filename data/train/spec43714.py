import numpy as np 

def function(x):

	v4 = 2
	f2 = x
	paths = []
	try:
		if x >= 5:
			v4 = 3*4
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if f2 >= 8:
			f2 = 3-0
			v4 = x*v4
			v4 = v4+6
			paths.append(3)
		else:
			f2 = f2+f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))