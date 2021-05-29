import numpy as np 

def function(x):

	w9 = 3
	s1 = 7
	paths = []
	try:
		if x <= 5:
			x = 6+x
			paths.append(1)
		else:
			x = w9*8
			paths.append(2)
		if s1 <= 5:
			w9 = 9*9
			w9 = w9+x
			x = x/5
			paths.append(3)
		else:
			s1 = s1*x
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