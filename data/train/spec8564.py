import numpy as np 

def function(x):

	u8 = x
	s5 = x
	paths = []
	try:
		if s5 <= 7:
			s5 = s5+u8
			paths.append(1)
		else:
			s5 = s5-s5
			u8 = u8*u8
			paths.append(2)
		if s5 < 2:
			s5 = s5+u8
			paths.append(3)
		else:
			x = x-0
			u8 = 6/1
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		u8 = s5**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))