import numpy as np 

def function(x):

	b4 = 2
	s0 = 6
	paths = []
	try:
		if x > 3:
			b4 = 5-b4
			s0 = s0-s0
			paths.append(1)
		else:
			s0 = 5*0
			x = 9/x
			paths.append(2)
		if b4 <= 1:
			x = x-5
			paths.append(3)
		else:
			s0 = x-1
			s0 = 5-x
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))