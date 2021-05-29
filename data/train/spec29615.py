import numpy as np 

def function(x):

	n5 = x
	u2 = 7
	paths = []
	try:
		if n5 <= 9:
			x = n5*2
			n5 = x+0
			u2 = 3+4
			paths.append(1)
		else:
			n5 = 2-n5
			u2 = 7/u2
			paths.append(2)
		if n5 > 7:
			n5 = n5+9
			x = x-5
			x = 3-x
			paths.append(3)
		else:
			x = 2-4
			n5 = 3/n5
			x = n5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))