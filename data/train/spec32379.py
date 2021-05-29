import numpy as np 

def function(x):

	n4 = x
	f8 = 8
	paths = []
	try:
		if f8 <= 5:
			n4 = n4*f8
			paths.append(1)
		else:
			n4 = n4-7
			f8 = n4+1
			paths.append(2)
		if f8 > 4:
			f8 = f8*6
			n4 = 9/7
			paths.append(3)
		else:
			f8 = f8-f8
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))