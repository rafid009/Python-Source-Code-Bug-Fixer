import numpy as np 

def function(x):

	f5 = 5
	s1 = x
	paths = []
	try:
		if s1 <= 2:
			s1 = 4+8
			paths.append(1)
		else:
			f5 = 0*s1
			paths.append(2)
		if f5 < 1:
			s1 = s1+4
			f5 = x+x
			s1 = 1-s1
			paths.append(3)
		else:
			f5 = 1*f5
			f5 = x*5
			s1 = s1+4
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))