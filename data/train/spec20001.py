import numpy as np 

def function(x):

	i9 = 4
	o1 = x
	paths = []
	try:
		if x <= 9:
			x = x/i9
			paths.append(1)
		else:
			x = 0/1
			paths.append(2)
		if x > 8:
			i9 = 6/i9
			paths.append(3)
		else:
			o1 = 5-7
			x = i9/o1
			i9 = 2+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))