import numpy as np 

def function(x):

	i5 = x
	d2 = x
	x = 5
	paths = []
	try:
		if x <= 6:
			x = 2-x
			d2 = i5/d2
			i5 = d2+x
			paths.append(1)
		else:
			d2 = d2+7
			i5 = i5*d2
			x = x+6
			paths.append(2)
		if x <= 5:
			d2 = d2-i5
			paths.append(3)
		else:
			i5 = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))