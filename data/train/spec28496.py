import numpy as np 

def function(x):

	f2 = 2
	v4 = 6
	paths = []
	try:
		if x < 0:
			x = 2/x
			f2 = x+f2
			paths.append(1)
		else:
			v4 = v4/v4
			paths.append(2)
		if f2 >= 6:
			v4 = v4*1
			v4 = v4-4
			f2 = f2/3
			paths.append(3)
		else:
			v4 = v4-5
			f2 = v4*f2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))