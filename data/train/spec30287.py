import numpy as np 

def function(x):

	u8 = 7
	a5 = x
	x = 6
	paths = []
	try:
		if x > 2:
			x = 7-1
			a5 = a5/u8
			paths.append(1)
		else:
			a5 = u8/a5
			x = u8-x
			a5 = 8-a5
			paths.append(2)
		if u8 < 0:
			x = x/8
			paths.append(3)
		else:
			u8 = u8+2
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))