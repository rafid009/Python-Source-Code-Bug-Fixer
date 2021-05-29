import numpy as np 

def function(x):

	s7 = x
	u8 = x
	x = 2
	paths = []
	try:
		if x > 5:
			x = 4-x
			u8 = u8*0
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if u8 <= 8:
			u8 = 0-5
			x = u8/x
			s7 = x*x
			paths.append(3)
		else:
			u8 = 0-6
			u8 = u8+2
			u8 = 6+3
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		u8 = u8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))