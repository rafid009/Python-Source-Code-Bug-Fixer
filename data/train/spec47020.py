import numpy as np 

def function(x):

	i4 = x
	l4 = 4
	paths = []
	try:
		if x <= 7:
			x = x+l4
			x = x/8
			paths.append(1)
		else:
			l4 = 5-l4
			l4 = l4*1
			paths.append(2)
		if x < 6:
			l4 = l4*x
			i4 = l4*i4
			i4 = i4/l4
			paths.append(3)
		else:
			i4 = 1*i4
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