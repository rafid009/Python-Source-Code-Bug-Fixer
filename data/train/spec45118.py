import numpy as np 

def function(x):

	l3 = x
	v6 = 1
	paths = []
	try:
		if v6 <= 6:
			l3 = l3/3
			x = v6/1
			paths.append(1)
		else:
			l3 = l3/4
			paths.append(2)
		if v6 < 2:
			x = v6-3
			paths.append(3)
		else:
			v6 = v6/2
			v6 = v6-1
			l3 = l3-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))