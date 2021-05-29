import numpy as np 

def function(x):

	k6 = 2
	f0 = 0
	paths = []
	try:
		if k6 > 4:
			k6 = k6/9
			f0 = 9*f0
			paths.append(1)
		else:
			k6 = f0-x
			f0 = 2*f0
			paths.append(2)
		if f0 <= 1:
			f0 = f0*1
			paths.append(3)
		else:
			f0 = k6-6
			f0 = 1/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))