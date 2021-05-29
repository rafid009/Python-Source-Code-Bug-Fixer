import numpy as np 

def function(x):

	r1 = 5
	s5 = 4
	paths = []
	try:
		if s5 >= 6:
			s5 = 7+s5
			r1 = r1/1
			r1 = 1-r1
			paths.append(1)
		else:
			r1 = r1*r1
			paths.append(2)
		if r1 <= 2:
			r1 = 3-r1
			r1 = r1+5
			paths.append(3)
		else:
			x = 4/x
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