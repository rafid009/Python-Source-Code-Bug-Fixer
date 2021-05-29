import numpy as np 

def function(x):

	s5 = x
	r1 = x
	paths = []
	try:
		if s5 >= 0:
			x = x*4
			paths.append(1)
		else:
			s5 = 1-9
			r1 = x/2
			s5 = s5/6
			paths.append(2)
		if r1 >= 9:
			x = 2/s5
			x = x*5
			x = 6/x
			paths.append(3)
		else:
			r1 = r1-3
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