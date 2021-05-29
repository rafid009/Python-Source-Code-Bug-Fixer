import numpy as np 

def function(x):

	s0 = 8
	f4 = 1
	paths = []
	try:
		if x < 4:
			f4 = x*f4
			f4 = x/7
			paths.append(1)
		else:
			x = x+3
			s0 = s0+s0
			f4 = s0*7
			paths.append(2)
		if f4 <= 0:
			x = s0+x
			x = 6+s0
			paths.append(3)
		else:
			x = 7+3
			s0 = 8-s0
			s0 = 5+8
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))