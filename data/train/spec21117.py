import numpy as np 

def function(x):

	u4 = 7
	f0 = 4
	x = x
	paths = []
	try:
		if f0 > 1:
			u4 = 5+x
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if x <= 2:
			f0 = x-2
			u4 = u4+9
			paths.append(3)
		else:
			f0 = f0+f0
			u4 = u4*6
			u4 = 4-0
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