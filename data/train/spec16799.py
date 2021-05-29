import numpy as np 

def function(x):

	s0 = x
	r7 = x
	paths = []
	try:
		if x <= 3:
			r7 = r7+x
			r7 = r7+5
			paths.append(1)
		else:
			r7 = r7*r7
			s0 = s0/s0
			r7 = r7*1
			paths.append(2)
		if s0 < 9:
			s0 = 8*s0
			paths.append(3)
		else:
			x = 4/s0
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		r7 = s0**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))