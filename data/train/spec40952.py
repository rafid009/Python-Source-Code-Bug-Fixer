import numpy as np 

def function(x):

	j6 = x
	l8 = x
	paths = []
	try:
		if x <= 8:
			j6 = j6*x
			x = x/1
			x = 3/l8
			paths.append(1)
		else:
			j6 = j6/2
			j6 = 9+l8
			paths.append(2)
		if l8 < 4:
			j6 = j6*6
			paths.append(3)
		else:
			l8 = 5-x
			l8 = l8-9
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