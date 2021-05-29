import numpy as np 

def function(x):

	a5 = 3
	u4 = x
	paths = []
	try:
		if a5 >= 7:
			a5 = a5*8
			a5 = x-9
			a5 = 1/2
			paths.append(1)
		else:
			x = 1*x
			x = 0+1
			a5 = a5*u4
			paths.append(2)
		if u4 <= 2:
			u4 = u4/x
			a5 = 0-a5
			x = x-9
			paths.append(3)
		else:
			a5 = a5/5
			u4 = u4*u4
			u4 = u4-4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))