import numpy as np 

def function(x):

	r2 = 4
	f6 = x
	paths = []
	try:
		if r2 < 7:
			x = x*f6
			r2 = f6+8
			r2 = 2-4
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if r2 < 8:
			r2 = 1/5
			x = r2-x
			x = 5-x
			paths.append(3)
		else:
			r2 = 0-5
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))