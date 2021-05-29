import numpy as np 

def function(x):

	s6 = x
	j5 = x
	paths = []
	try:
		if x > 5:
			s6 = s6+0
			s6 = 6*x
			paths.append(1)
		else:
			s6 = s6/8
			paths.append(2)
		if j5 >= 4:
			s6 = 1/s6
			x = x*3
			s6 = j5*4
			paths.append(3)
		else:
			s6 = s6/5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		s6 = j5**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))