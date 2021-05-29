import numpy as np 

def function(x):

	s9 = 4
	i5 = 0
	paths = []
	try:
		if x > 1:
			s9 = 1-s9
			s9 = 4-s9
			x = x*8
			paths.append(1)
		else:
			i5 = i5*s9
			s9 = s9-0
			paths.append(2)
		if i5 < 9:
			i5 = 0*4
			s9 = i5-8
			i5 = 5+3
			paths.append(3)
		else:
			s9 = 8-x
			s9 = 1/s9
			s9 = s9-1
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))