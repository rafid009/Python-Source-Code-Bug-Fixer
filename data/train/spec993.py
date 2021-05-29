import numpy as np 

def function(x):

	f7 = 6
	o2 = x
	paths = []
	try:
		if x < 9:
			x = 1-f7
			f7 = 4+o2
			paths.append(1)
		else:
			x = 3+x
			o2 = 7/f7
			paths.append(2)
		if x < 7:
			o2 = f7+o2
			f7 = f7/3
			x = x-5
			paths.append(3)
		else:
			f7 = f7-4
			x = 1-x
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))