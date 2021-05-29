import numpy as np 

def function(x):

	e2 = 6
	k6 = 6
	paths = []
	try:
		if e2 <= 6:
			x = x-2
			k6 = k6*e2
			k6 = e2*k6
			paths.append(1)
		else:
			k6 = 7-k6
			e2 = e2+2
			paths.append(2)
		if x > 7:
			x = x*k6
			e2 = e2/6
			paths.append(3)
		else:
			x = x/8
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