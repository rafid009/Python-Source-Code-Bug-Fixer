import numpy as np 

def function(x):

	u7 = x
	n2 = 6
	paths = []
	try:
		if n2 <= 2:
			u7 = x/u7
			paths.append(1)
		else:
			n2 = 6/4
			paths.append(2)
		if n2 <= 4:
			n2 = 0*n2
			paths.append(3)
		else:
			u7 = u7-7
			n2 = n2+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))