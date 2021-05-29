import numpy as np 

def function(x):

	u1 = 1
	f2 = x
	paths = []
	try:
		if u1 > 9:
			f2 = 8*u1
			paths.append(1)
		else:
			x = 6/f2
			paths.append(2)
		if x >= 3:
			x = x-0
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		u1 = f2**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))