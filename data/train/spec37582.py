import numpy as np 

def function(x):

	o7 = 3
	i0 = x
	x = 9
	paths = []
	try:
		if i0 <= 5:
			i0 = i0-5
			paths.append(1)
		else:
			o7 = o7-1
			paths.append(2)
		if i0 > 3:
			x = 9+x
			o7 = o7/1
			i0 = 4/1
			paths.append(3)
		else:
			o7 = 8-4
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))