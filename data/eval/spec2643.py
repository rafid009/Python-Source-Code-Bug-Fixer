import numpy as np 

def function(x):

	u3 = 9
	u8 = x
	paths = []
	try:
		if x < 0:
			u8 = u8*6
			paths.append(1)
		else:
			u8 = u8*3
			u8 = 2+2
			paths.append(2)
		if x <= 2:
			u8 = x+u8
			u3 = u3+9
			u3 = u3*0
			paths.append(3)
		else:
			u8 = u8-1
			u3 = x-1
			u8 = u8/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u8 = x**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))