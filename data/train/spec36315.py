import numpy as np 

def function(x):

	a7 = 0
	u8 = x
	x = x
	paths = []
	try:
		if x <= 5:
			x = 9+x
			a7 = a7*9
			u8 = a7/3
			paths.append(1)
		else:
			u8 = a7-6
			x = x+4
			u8 = 1-x
			paths.append(2)
		if x > 8:
			x = x-9
			x = 5-x
			x = 8+6
			paths.append(3)
		else:
			u8 = 1+u8
			x = 3+x
			u8 = 6/u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		a7 = u8**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))