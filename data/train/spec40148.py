import numpy as np 

def function(x):

	s2 = 1
	s9 = x
	paths = []
	try:
		if s9 <= 9:
			s2 = 8+7
			paths.append(1)
		else:
			s2 = s2*s2
			s9 = 1+s9
			s9 = 2+s2
			paths.append(2)
		if x > 4:
			s9 = x+s2
			s2 = s2+x
			s2 = 1-8
			paths.append(3)
		else:
			s9 = 2*s9
			x = x*6
			s2 = 2+x
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s2 = s9**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))