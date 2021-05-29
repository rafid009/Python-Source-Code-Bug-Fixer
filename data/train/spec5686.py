import numpy as np 

def function(x):

	f6 = x
	o7 = 1
	x = 2
	paths = []
	try:
		if x >= 5:
			o7 = 5+o7
			paths.append(1)
		else:
			f6 = 3/f6
			paths.append(2)
		if f6 >= 9:
			x = 0-x
			f6 = 4/o7
			paths.append(3)
		else:
			o7 = o7*8
			f6 = f6-o7
			x = 7-9
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		o7 = f6**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))