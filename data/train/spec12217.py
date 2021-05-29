import numpy as np 

def function(x):

	s5 = 1
	s4 = 4
	paths = []
	try:
		if s5 > 0:
			x = x-4
			paths.append(1)
		else:
			s4 = s4+4
			s4 = 1+x
			s4 = x*8
			paths.append(2)
		if s5 > 3:
			x = x-s4
			x = x-7
			s5 = 8*s5
			paths.append(3)
		else:
			s4 = s4/6
			s4 = x/s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))