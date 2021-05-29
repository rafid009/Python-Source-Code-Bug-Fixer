import numpy as np 

def function(x):

	v0 = x
	i8 = 8
	paths = []
	try:
		if v0 <= 4:
			x = x*3
			paths.append(1)
		else:
			i8 = 5+i8
			paths.append(2)
		if x > 4:
			v0 = v0/x
			i8 = 7*i8
			x = 9/x
			paths.append(3)
		else:
			v0 = v0-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))