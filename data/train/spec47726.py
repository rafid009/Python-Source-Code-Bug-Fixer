import numpy as np 

def function(x):

	r0 = 4
	s6 = x
	paths = []
	try:
		if s6 > 7:
			s6 = s6*2
			s6 = s6+5
			s6 = s6/s6
			paths.append(1)
		else:
			s6 = 6-s6
			paths.append(2)
		if x >= 1:
			x = 2*r0
			x = x-8
			r0 = r0+r0
			paths.append(3)
		else:
			s6 = s6*2
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		r0 = s6**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))