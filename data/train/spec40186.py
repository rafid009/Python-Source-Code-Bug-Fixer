import numpy as np 

def function(x):

	f8 = 1
	v0 = 2
	paths = []
	try:
		if x > 8:
			f8 = v0/x
			x = 7/6
			paths.append(1)
		else:
			v0 = 6+v0
			paths.append(2)
		if v0 <= 7:
			f8 = 4+f8
			paths.append(3)
		else:
			v0 = x*v0
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