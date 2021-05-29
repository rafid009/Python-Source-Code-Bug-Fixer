import numpy as np 

def function(x):

	s5 = x
	s6 = x
	x = x
	paths = []
	try:
		if s6 < 1:
			s5 = s5+s6
			s6 = s6-s5
			paths.append(1)
		else:
			x = x/3
			x = 6+9
			s5 = s5/8
			paths.append(2)
		if s6 >= 8:
			s5 = 2*s6
			paths.append(3)
		else:
			s5 = s5+0
			s5 = x+s5
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))