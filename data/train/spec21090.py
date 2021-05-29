import numpy as np 

def function(x):

	f9 = 8
	v3 = 6
	x = x
	paths = []
	try:
		if v3 > 7:
			v3 = v3*x
			x = 9*x
			paths.append(1)
		else:
			f9 = f9-v3
			paths.append(2)
		if f9 >= 5:
			x = 1+6
			v3 = f9/v3
			v3 = 5/9
			paths.append(3)
		else:
			f9 = 3+0
			f9 = v3+1
			v3 = 8-x
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