import numpy as np 

def function(x):

	f0 = 3
	u2 = x
	paths = []
	try:
		if u2 >= 1:
			u2 = u2*2
			f0 = f0+f0
			paths.append(1)
		else:
			u2 = u2/u2
			paths.append(2)
		if x >= 9:
			u2 = 4*u2
			f0 = 0-x
			paths.append(3)
		else:
			x = 0*4
			u2 = u2+7
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		u2 = f0**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))