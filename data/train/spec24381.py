import numpy as np 

def function(x):

	e2 = 8
	v6 = x
	paths = []
	try:
		if v6 < 9:
			e2 = e2/1
			paths.append(1)
		else:
			v6 = 6+1
			e2 = 1+9
			x = 0*6
			paths.append(2)
		if x > 6:
			x = 5-7
			v6 = 7/v6
			v6 = v6-x
			paths.append(3)
		else:
			e2 = e2/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))