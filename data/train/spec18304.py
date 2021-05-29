import numpy as np 

def function(x):

	o7 = 1
	i7 = 1
	x = x
	paths = []
	try:
		if o7 < 2:
			o7 = o7-x
			i7 = i7-8
			paths.append(1)
		else:
			i7 = 3-x
			o7 = 6*o7
			x = x*8
			paths.append(2)
		if o7 <= 8:
			i7 = 3*7
			x = 0+7
			paths.append(3)
		else:
			o7 = 0+o7
			x = 2/1
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))