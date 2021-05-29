import numpy as np 

def function(x):

	i4 = 7
	l3 = 6
	paths = []
	try:
		if x <= 9:
			i4 = 6+i4
			l3 = 9+l3
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x <= 1:
			i4 = l3*i4
			paths.append(3)
		else:
			i4 = 9-i4
			l3 = l3*x
			i4 = i4/i4
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