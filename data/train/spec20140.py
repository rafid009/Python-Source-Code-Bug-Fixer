import numpy as np 

def function(x):

	s0 = x
	u8 = x
	paths = []
	try:
		if s0 <= 4:
			u8 = u8-1
			s0 = s0+1
			s0 = x*5
			paths.append(1)
		else:
			x = s0*9
			x = x+s0
			s0 = 0/s0
			paths.append(2)
		if s0 >= 0:
			u8 = u8-7
			x = x-8
			paths.append(3)
		else:
			s0 = 6*1
			s0 = s0*s0
			s0 = s0*8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))