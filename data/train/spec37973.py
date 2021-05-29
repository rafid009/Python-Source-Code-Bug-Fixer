import numpy as np 

def function(x):

	v2 = 7
	u8 = x
	paths = []
	try:
		if v2 < 7:
			v2 = v2*6
			paths.append(1)
		else:
			u8 = u8/v2
			u8 = u8-x
			x = 7/x
			paths.append(2)
		if x >= 9:
			v2 = v2-4
			x = x/x
			x = 0*x
			paths.append(3)
		else:
			x = x+x
			x = x*x
			v2 = 0-u8
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		u8 = v2**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))