import numpy as np 

def function(x):

	i0 = 0
	u7 = 1
	paths = []
	try:
		if x > 7:
			u7 = u7+5
			paths.append(1)
		else:
			x = u7*x
			x = 1*x
			paths.append(2)
		if x <= 9:
			i0 = 5-i0
			paths.append(3)
		else:
			x = i0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))