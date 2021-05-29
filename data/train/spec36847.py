import numpy as np 

def function(x):

	i5 = x
	u8 = 3
	paths = []
	try:
		if x > 0:
			x = x-7
			paths.append(1)
		else:
			i5 = x/i5
			u8 = 6+u8
			paths.append(2)
		if u8 >= 0:
			u8 = x-6
			u8 = 5+u8
			i5 = 5-3
			paths.append(3)
		else:
			u8 = i5/u8
			i5 = 6/i5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))