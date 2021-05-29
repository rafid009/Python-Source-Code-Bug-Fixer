import numpy as np 

def function(x):

	i6 = 6
	e6 = x
	paths = []
	try:
		if i6 < 4:
			e6 = x/e6
			x = e6/x
			e6 = e6-1
			paths.append(1)
		else:
			e6 = e6+i6
			i6 = i6+i6
			paths.append(2)
		if e6 < 8:
			e6 = 0/e6
			paths.append(3)
		else:
			e6 = e6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))