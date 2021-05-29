import numpy as np 

def function(x):

	f3 = x
	k6 = 9
	paths = []
	try:
		if x > 3:
			f3 = 0/9
			f3 = f3+5
			paths.append(1)
		else:
			f3 = 5*k6
			paths.append(2)
		if k6 > 1:
			f3 = f3/5
			k6 = 0+k6
			f3 = 0*k6
			paths.append(3)
		else:
			x = f3-5
			x = 8-4
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