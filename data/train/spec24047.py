import numpy as np 

def function(x):

	u2 = x
	f6 = x
	paths = []
	try:
		if u2 <= 8:
			f6 = 4+6
			paths.append(1)
		else:
			x = x/7
			u2 = u2-3
			paths.append(2)
		if x >= 2:
			u2 = 6/u2
			u2 = u2-1
			paths.append(3)
		else:
			x = x-0
			x = 9/f6
			u2 = u2+f6
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))