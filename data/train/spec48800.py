import numpy as np 

def function(x):

	w7 = x
	s2 = x
	paths = []
	try:
		if x > 2:
			s2 = 1-s2
			w7 = x*w7
			x = 0*0
			paths.append(1)
		else:
			w7 = 0*w7
			x = x+x
			paths.append(2)
		if x >= 8:
			s2 = s2-4
			x = x-5
			paths.append(3)
		else:
			s2 = s2*9
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