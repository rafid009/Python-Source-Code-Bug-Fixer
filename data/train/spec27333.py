import numpy as np 

def function(x):

	f6 = x
	r0 = x
	paths = []
	try:
		if f6 < 5:
			x = x-x
			r0 = f6-r0
			f6 = f6/2
			paths.append(1)
		else:
			f6 = f6-4
			paths.append(2)
		if x < 5:
			r0 = 6/6
			r0 = r0-7
			f6 = 3/6
			paths.append(3)
		else:
			r0 = 5-3
			f6 = f6*x
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))