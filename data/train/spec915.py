import numpy as np 

def function(x):

	p7 = x
	f8 = x
	paths = []
	try:
		if f8 < 2:
			x = x-9
			x = 0/8
			x = f8-0
			paths.append(1)
		else:
			p7 = 7/p7
			x = f8/4
			f8 = f8*f8
			paths.append(2)
		if p7 >= 3:
			x = 1*4
			p7 = f8+6
			x = x-7
			paths.append(3)
		else:
			x = f8+6
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))