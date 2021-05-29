import numpy as np 

def function(x):

	f7 = x
	q8 = 9
	paths = []
	try:
		if x >= 4:
			f7 = f7+x
			x = q8*x
			x = 0-0
			paths.append(1)
		else:
			q8 = 4/q8
			q8 = q8*7
			f7 = 1*f7
			paths.append(2)
		if q8 <= 9:
			q8 = 4*x
			x = x+f7
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))