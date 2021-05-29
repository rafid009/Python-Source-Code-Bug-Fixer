import numpy as np 

def function(x):

	t3 = 7
	s1 = x
	x = 6
	paths = []
	try:
		if x > 1:
			x = 9+s1
			paths.append(1)
		else:
			t3 = x*t3
			paths.append(2)
		if t3 >= 6:
			s1 = s1-7
			t3 = t3+x
			x = x*s1
			paths.append(3)
		else:
			t3 = 7/t3
			s1 = s1-9
			x = t3*t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))