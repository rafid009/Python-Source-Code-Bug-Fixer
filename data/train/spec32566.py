import numpy as np 

def function(x):

	y8 = 2
	f4 = 9
	x = 1
	paths = []
	try:
		if f4 >= 9:
			f4 = f4/3
			x = x/1
			paths.append(1)
		else:
			y8 = 5/5
			paths.append(2)
		if x <= 9:
			f4 = 4-f4
			y8 = y8-8
			paths.append(3)
		else:
			x = 9-x
			f4 = f4+f4
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))