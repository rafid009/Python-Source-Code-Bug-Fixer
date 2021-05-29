import numpy as np 

def function(x):

	s6 = 9
	j2 = x
	paths = []
	try:
		if j2 <= 6:
			x = x+j2
			j2 = j2-s6
			paths.append(1)
		else:
			s6 = s6-j2
			x = 5*s6
			s6 = 5+s6
			paths.append(2)
		if x < 0:
			x = 1*1
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))