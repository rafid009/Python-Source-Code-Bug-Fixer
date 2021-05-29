import numpy as np 

def function(x):

	v3 = 5
	e6 = x
	x = x
	paths = []
	try:
		if v3 > 0:
			x = 5*x
			paths.append(1)
		else:
			v3 = v3+x
			paths.append(2)
		if e6 > 1:
			v3 = 2-x
			e6 = 7-4
			paths.append(3)
		else:
			e6 = v3+7
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		e6 = v3**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))