import numpy as np 

def function(x):

	s6 = 3
	i9 = 3
	paths = []
	try:
		if x < 3:
			x = x-4
			i9 = 2-i9
			paths.append(1)
		else:
			i9 = s6+i9
			paths.append(2)
		if s6 < 6:
			i9 = x+9
			x = 6/7
			x = x*1
			paths.append(3)
		else:
			s6 = 4+s6
			s6 = 3+s6
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		s6 = i9**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))