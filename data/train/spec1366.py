import numpy as np 

def function(x):

	s2 = 4
	j4 = x
	paths = []
	try:
		if j4 < 2:
			x = x-4
			j4 = j4-x
			j4 = s2*0
			paths.append(1)
		else:
			x = x/3
			s2 = j4-s2
			paths.append(2)
		if j4 > 4:
			s2 = s2/2
			j4 = j4/j4
			s2 = s2*9
			paths.append(3)
		else:
			x = x*0
			s2 = 8*s2
			j4 = s2+j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		s2 = j4**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))