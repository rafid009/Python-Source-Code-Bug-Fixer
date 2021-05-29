import numpy as np 

def function(x):

	i0 = 9
	i5 = 4
	paths = []
	try:
		if i5 <= 7:
			i5 = i5/7
			i0 = 8/i0
			paths.append(1)
		else:
			x = 9/i5
			paths.append(2)
		if i5 <= 7:
			i0 = i0*x
			paths.append(3)
		else:
			x = x+5
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