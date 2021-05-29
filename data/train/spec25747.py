import numpy as np 

def function(x):

	v3 = x
	e9 = 5
	paths = []
	try:
		if v3 <= 5:
			e9 = 4+e9
			x = x+v3
			paths.append(1)
		else:
			e9 = v3*x
			paths.append(2)
		if e9 > 5:
			v3 = v3-x
			v3 = e9/1
			paths.append(3)
		else:
			e9 = e9/e9
			v3 = 5-v3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))