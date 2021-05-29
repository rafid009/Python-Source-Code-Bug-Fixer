import numpy as np 

def function(x):

	e8 = x
	j6 = x
	paths = []
	try:
		if e8 > 8:
			x = x*6
			j6 = x+8
			paths.append(1)
		else:
			e8 = 9-e8
			paths.append(2)
		if x < 0:
			j6 = e8*5
			paths.append(3)
		else:
			e8 = 7*e8
			e8 = 0*e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))