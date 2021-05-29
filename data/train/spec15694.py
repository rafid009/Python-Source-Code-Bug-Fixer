import numpy as np 

def function(x):

	i6 = 0
	o7 = 0
	paths = []
	try:
		if o7 > 5:
			i6 = 6-i6
			x = 5-1
			paths.append(1)
		else:
			i6 = i6-0
			o7 = o7-o7
			i6 = 3+i6
			paths.append(2)
		if i6 > 3:
			o7 = o7/i6
			x = 9-x
			paths.append(3)
		else:
			o7 = 2+o7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))