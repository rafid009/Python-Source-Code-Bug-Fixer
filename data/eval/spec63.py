import numpy as np 

def function(x):

	i4 = x
	x7 = x
	x = x
	paths = []
	try:
		if x7 > 4:
			i4 = i4+9
			i4 = 2-8
			i4 = 7+i4
			paths.append(1)
		else:
			x7 = x7+6
			x7 = 7-2
			x = 1-8
			paths.append(2)
		if i4 < 4:
			x = x+x7
			i4 = 6-8
			paths.append(3)
		else:
			x7 = 3/x7
			x = i4/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))