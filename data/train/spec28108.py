import numpy as np 

def function(x):

	e6 = x
	k8 = x
	paths = []
	try:
		if x > 1:
			e6 = 3*x
			x = x-9
			paths.append(1)
		else:
			x = 6/6
			e6 = 9-e6
			x = x-6
			paths.append(2)
		if k8 >= 6:
			e6 = 5/1
			x = 2-4
			paths.append(3)
		else:
			e6 = 0-e6
			k8 = k8+9
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))