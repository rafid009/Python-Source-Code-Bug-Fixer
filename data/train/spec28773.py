import numpy as np 

def function(x):

	u5 = 8
	a0 = x
	paths = []
	try:
		if a0 >= 3:
			x = 2+x
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x >= 7:
			x = 8+x
			u5 = a0/u5
			a0 = 5+a0
			paths.append(3)
		else:
			a0 = a0+a0
			x = a0+2
			u5 = x-5
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		u5 = a0**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))