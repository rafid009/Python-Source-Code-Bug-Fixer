import numpy as np 

def function(x):

	u2 = x
	x8 = 3
	paths = []
	try:
		if u2 > 4:
			x = x8+8
			paths.append(1)
		else:
			u2 = x+7
			u2 = 1-7
			paths.append(2)
		if x > 4:
			x = u2-7
			x8 = x8-x8
			x = x+2
			paths.append(3)
		else:
			x = x/1
			u2 = 8*u2
			u2 = u2*3
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x8 = u2**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))