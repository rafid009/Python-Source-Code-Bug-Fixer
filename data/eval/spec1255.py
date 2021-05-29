import numpy as np 

def function(x):

	f6 = 6
	s4 = x
	paths = []
	try:
		if s4 <= 4:
			x = x*x
			paths.append(1)
		else:
			x = x*x
			f6 = x-9
			paths.append(2)
		if s4 >= 3:
			f6 = 2-x
			s4 = x*8
			paths.append(3)
		else:
			f6 = 6+x
			x = x+x
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