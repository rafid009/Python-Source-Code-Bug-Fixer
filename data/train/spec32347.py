import numpy as np 

def function(x):

	e7 = x
	u8 = x
	paths = []
	try:
		if x < 4:
			u8 = u8-0
			e7 = 6+9
			paths.append(1)
		else:
			e7 = u8+e7
			x = u8/6
			paths.append(2)
		if u8 >= 2:
			u8 = 4-u8
			paths.append(3)
		else:
			e7 = e7*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))