import numpy as np 

def function(x):

	e6 = 6
	v8 = x
	paths = []
	try:
		if x >= 0:
			v8 = v8-e6
			e6 = e6-2
			x = 8-x
			paths.append(1)
		else:
			e6 = 5+e6
			e6 = e6+7
			paths.append(2)
		if x <= 6:
			x = 2/x
			v8 = e6+2
			paths.append(3)
		else:
			v8 = e6/1
			e6 = e6-x
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