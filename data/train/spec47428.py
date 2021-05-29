import numpy as np 

def function(x):

	s1 = 7
	r5 = x
	paths = []
	try:
		if x >= 9:
			s1 = 7+r5
			r5 = 5/x
			paths.append(1)
		else:
			s1 = s1*1
			paths.append(2)
		if r5 < 2:
			s1 = 9*s1
			s1 = s1-r5
			paths.append(3)
		else:
			s1 = s1-7
			r5 = 5*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))