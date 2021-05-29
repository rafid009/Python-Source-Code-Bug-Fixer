import numpy as np 

def function(x):

	j9 = 0
	e8 = x
	paths = []
	try:
		if e8 > 0:
			e8 = j9*9
			paths.append(1)
		else:
			e8 = e8-4
			paths.append(2)
		if x > 4:
			e8 = 0*e8
			paths.append(3)
		else:
			j9 = j9*x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))