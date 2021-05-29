import numpy as np 

def function(x):

	s4 = x
	f9 = 6
	paths = []
	try:
		if x < 2:
			x = 4+x
			s4 = x-4
			paths.append(1)
		else:
			s4 = 0+s4
			s4 = s4-x
			s4 = s4+9
			paths.append(2)
		if f9 >= 7:
			s4 = x+s4
			s4 = 2-s4
			x = f9/x
			paths.append(3)
		else:
			s4 = s4+3
			x = 1+x
			f9 = 0-x
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		s4 = f9**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))