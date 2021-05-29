import numpy as np 

def function(x):

	s5 = x
	j2 = 7
	paths = []
	try:
		if s5 <= 5:
			s5 = s5+2
			paths.append(1)
		else:
			j2 = 1/j2
			x = j2+x
			paths.append(2)
		if s5 < 4:
			x = 8-x
			paths.append(3)
		else:
			x = 1*s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))