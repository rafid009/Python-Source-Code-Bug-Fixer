import numpy as np 

def function(x):

	i4 = x
	d6 = x
	x = 9
	paths = []
	try:
		if x >= 9:
			i4 = 9/i4
			d6 = 5+i4
			paths.append(1)
		else:
			x = 3-x
			i4 = i4-7
			paths.append(2)
		if i4 > 8:
			d6 = i4-6
			paths.append(3)
		else:
			x = i4/9
			d6 = d6-d6
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))