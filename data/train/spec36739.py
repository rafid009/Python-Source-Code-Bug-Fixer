import numpy as np 

def function(x):

	r2 = x
	s1 = x
	paths = []
	try:
		if s1 > 5:
			x = s1/6
			paths.append(1)
		else:
			s1 = s1/r2
			r2 = r2+x
			paths.append(2)
		if x >= 2:
			s1 = s1+s1
			s1 = 6-r2
			r2 = r2-0
			paths.append(3)
		else:
			s1 = s1/s1
			x = 5/r2
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