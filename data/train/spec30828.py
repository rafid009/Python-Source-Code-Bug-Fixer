import numpy as np 

def function(x):

	k6 = 0
	e7 = 9
	paths = []
	try:
		if x < 8:
			e7 = 0/e7
			x = x/9
			k6 = e7*e7
			paths.append(1)
		else:
			x = 0*x
			e7 = e7+7
			e7 = k6+e7
			paths.append(2)
		if e7 >= 1:
			x = x+x
			paths.append(3)
		else:
			x = x-e7
			x = 2+x
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