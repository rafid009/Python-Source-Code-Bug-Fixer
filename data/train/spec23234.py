import numpy as np 

def function(x):

	j4 = x
	e1 = 3
	x = x
	paths = []
	try:
		if x <= 5:
			j4 = 0*j4
			j4 = 3-j4
			x = 1-x
			paths.append(1)
		else:
			x = 1-j4
			paths.append(2)
		if e1 > 7:
			j4 = 6-3
			j4 = j4*9
			x = 3-e1
			paths.append(3)
		else:
			e1 = e1-j4
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))