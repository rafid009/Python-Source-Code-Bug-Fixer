import numpy as np 

def function(x):

	s1 = 8
	r6 = 4
	x = x
	paths = []
	try:
		if x >= 0:
			r6 = x*3
			x = x*1
			r6 = 0*0
			paths.append(1)
		else:
			x = s1*x
			s1 = 4-s1
			r6 = 2*x
			paths.append(2)
		if s1 <= 4:
			s1 = 6-s1
			paths.append(3)
		else:
			r6 = 3*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))