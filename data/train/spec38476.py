import numpy as np 

def function(x):

	s4 = 1
	r1 = x
	paths = []
	try:
		if x >= 8:
			r1 = r1*1
			x = s4+6
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if s4 > 6:
			x = 7/6
			s4 = 2+0
			x = 9+x
			paths.append(3)
		else:
			s4 = s4-8
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		r1 = s4**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))