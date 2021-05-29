import numpy as np 

def function(x):

	i4 = x
	o6 = 8
	paths = []
	try:
		if x <= 1:
			i4 = i4+i4
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x > 6:
			i4 = o6+i4
			i4 = x*i4
			x = 1/x
			paths.append(3)
		else:
			o6 = o6+o6
			x = 8-o6
			i4 = 2*i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))