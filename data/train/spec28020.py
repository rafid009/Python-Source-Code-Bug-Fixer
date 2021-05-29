import numpy as np 

def function(x):

	r8 = x
	s5 = 5
	paths = []
	try:
		if x < 4:
			r8 = r8/x
			r8 = 7/x
			paths.append(1)
		else:
			x = x-8
			r8 = 2*r8
			paths.append(2)
		if x > 6:
			r8 = r8*5
			s5 = x/s5
			s5 = 3*s5
			paths.append(3)
		else:
			s5 = r8+s5
			s5 = 8+s5
			s5 = 7/s5
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