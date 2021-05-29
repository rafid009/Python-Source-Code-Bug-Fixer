import numpy as np 

def function(x):

	o4 = 2
	s1 = x
	x = 9
	paths = []
	try:
		if x < 3:
			o4 = o4*0
			paths.append(1)
		else:
			o4 = 0+o4
			paths.append(2)
		if s1 <= 8:
			o4 = 2-o4
			paths.append(3)
		else:
			s1 = s1/x
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))