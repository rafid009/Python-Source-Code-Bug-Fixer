import numpy as np 

def function(x):

	s2 = 9
	v1 = 3
	x = x
	paths = []
	try:
		if x >= 0:
			v1 = v1+6
			x = 0*8
			paths.append(1)
		else:
			v1 = v1-5
			x = x*s2
			s2 = s2*s2
			paths.append(2)
		if s2 > 9:
			v1 = v1/9
			s2 = v1*s2
			paths.append(3)
		else:
			x = 2*0
			x = x/3
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))