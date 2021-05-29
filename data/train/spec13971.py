import numpy as np 

def function(x):

	u8 = 9
	v7 = x
	paths = []
	try:
		if v7 >= 7:
			u8 = u8+v7
			v7 = x+3
			paths.append(1)
		else:
			x = x/u8
			u8 = u8+x
			paths.append(2)
		if v7 <= 1:
			u8 = 9-u8
			paths.append(3)
		else:
			x = 5*x
			v7 = v7+8
			x = 3-v7
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		v7 = u8**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))