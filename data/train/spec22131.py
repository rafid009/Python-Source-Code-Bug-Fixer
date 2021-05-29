import numpy as np 

def function(x):

	e0 = x
	v1 = 6
	paths = []
	try:
		if x < 8:
			e0 = e0+7
			x = x-2
			v1 = v1/v1
			paths.append(1)
		else:
			e0 = 7+e0
			x = x-6
			paths.append(2)
		if e0 <= 9:
			e0 = x+e0
			paths.append(3)
		else:
			e0 = e0/3
			x = x-e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		v1 = e0**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))