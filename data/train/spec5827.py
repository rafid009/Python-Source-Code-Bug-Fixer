import numpy as np 

def function(x):

	s5 = 5
	u8 = x
	paths = []
	try:
		if u8 >= 6:
			u8 = 0/u8
			s5 = 0+u8
			paths.append(1)
		else:
			u8 = u8*s5
			x = 5-8
			paths.append(2)
		if u8 >= 4:
			x = s5-s5
			paths.append(3)
		else:
			u8 = 2-5
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