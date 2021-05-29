import numpy as np 

def function(x):

	s5 = 2
	f8 = 7
	paths = []
	try:
		if s5 <= 1:
			x = f8*x
			x = 1/f8
			s5 = s5*3
			paths.append(1)
		else:
			x = 4*x
			f8 = s5+x
			f8 = 6-f8
			paths.append(2)
		if x < 2:
			x = x-0
			s5 = s5/x
			f8 = f8/4
			paths.append(3)
		else:
			f8 = f8-f8
			x = f8+x
			s5 = s5/2
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))