import numpy as np 

def function(x):

	s0 = x
	f7 = 0
	paths = []
	try:
		if f7 <= 6:
			f7 = f7+f7
			x = 0+x
			paths.append(1)
		else:
			s0 = 2-x
			x = s0+x
			f7 = 6*f7
			paths.append(2)
		if s0 > 0:
			s0 = s0+x
			s0 = s0+f7
			paths.append(3)
		else:
			s0 = s0+f7
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