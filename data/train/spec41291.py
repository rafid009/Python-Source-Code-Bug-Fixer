import numpy as np 

def function(x):

	s0 = 5
	f7 = x
	x = 6
	paths = []
	try:
		if x < 1:
			x = x+9
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if x >= 6:
			s0 = 0-s0
			paths.append(3)
		else:
			f7 = 0/9
			f7 = 7*f7
			f7 = 9-2
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		f7 = s0**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))