import numpy as np 

def function(x):

	f9 = x
	s2 = x
	paths = []
	try:
		if s2 < 4:
			s2 = 5*s2
			paths.append(1)
		else:
			f9 = 7*s2
			paths.append(2)
		if x <= 7:
			s2 = 8+x
			paths.append(3)
		else:
			s2 = 5*1
			x = s2/5
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		s2 = f9**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))