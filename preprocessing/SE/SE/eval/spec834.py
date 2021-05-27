import numpy as np 

def function(x):

	u8 = 8
	s4 = 6
	paths = []
	try:
		if x <= 0:
			x = 4*8
			paths.append(1)
		else:
			s4 = s4*u8
			paths.append(2)
		if u8 >= 7:
			s4 = 5+s4
			u8 = 0-u8
			s4 = u8*s4
			paths.append(3)
		else:
			u8 = x/u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		s4 = u8**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))