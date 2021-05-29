import numpy as np 

def function(x):

	f1 = 8
	f6 = x
	paths = []
	try:
		if x <= 7:
			f1 = 9*2
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if f6 > 8:
			x = x-x
			paths.append(3)
		else:
			f6 = 8*f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))