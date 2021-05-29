import numpy as np 

def function(x):

	d0 = 3
	i5 = x
	paths = []
	try:
		if i5 > 9:
			d0 = i5-x
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if x > 2:
			x = 8+5
			d0 = d0/3
			paths.append(3)
		else:
			x = d0+6
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))