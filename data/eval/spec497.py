import numpy as np 

def function(x):

	v9 = x
	e1 = 4
	x = 8
	paths = []
	try:
		if e1 >= 5:
			e1 = 8*9
			e1 = 9*e1
			e1 = 9+e1
			paths.append(1)
		else:
			x = v9-v9
			v9 = v9+7
			v9 = v9*v9
			paths.append(2)
		if e1 >= 8:
			e1 = x*e1
			paths.append(3)
		else:
			e1 = x-e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		v9 = e1**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))