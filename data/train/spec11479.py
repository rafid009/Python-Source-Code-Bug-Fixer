import numpy as np 

def function(x):

	u2 = x
	f4 = x
	x = x
	paths = []
	try:
		if x > 3:
			u2 = 1*u2
			x = 2-f4
			f4 = 4/7
			paths.append(1)
		else:
			x = x-1
			x = x+4
			paths.append(2)
		if u2 <= 6:
			u2 = 1/u2
			f4 = u2-u2
			paths.append(3)
		else:
			x = 2*1
			x = x/2
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))