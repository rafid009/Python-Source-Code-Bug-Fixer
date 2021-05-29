import numpy as np 

def function(x):

	f3 = 1
	u8 = 0
	paths = []
	try:
		if u8 > 0:
			f3 = f3/9
			paths.append(1)
		else:
			u8 = 5/f3
			paths.append(2)
		if x >= 6:
			f3 = f3/1
			f3 = 4-f3
			u8 = u8*4
			paths.append(3)
		else:
			f3 = f3+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))