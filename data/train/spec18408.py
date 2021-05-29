import numpy as np 

def function(x):

	e8 = x
	v3 = 3
	paths = []
	try:
		if v3 <= 2:
			e8 = e8+x
			paths.append(1)
		else:
			x = v3+4
			paths.append(2)
		if x <= 7:
			x = x-x
			e8 = e8+e8
			paths.append(3)
		else:
			v3 = 0+8
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))