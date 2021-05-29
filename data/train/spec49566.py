import numpy as np 

def function(x):

	f8 = x
	v0 = 6
	paths = []
	try:
		if x > 0:
			x = x*3
			x = x*x
			paths.append(1)
		else:
			f8 = f8-6
			f8 = f8/3
			paths.append(2)
		if f8 > 3:
			x = 0/x
			paths.append(3)
		else:
			v0 = 2/f8
			x = f8+3
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		v0 = f8**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))