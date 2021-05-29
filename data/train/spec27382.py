import numpy as np 

def function(x):

	t0 = x
	s9 = x
	paths = []
	try:
		if t0 <= 3:
			x = x+t0
			x = 7*x
			paths.append(1)
		else:
			s9 = s9/2
			s9 = 3+s9
			paths.append(2)
		if t0 >= 4:
			s9 = 7*s9
			t0 = 9+3
			x = x/t0
			paths.append(3)
		else:
			s9 = s9*3
			t0 = 3-t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		s9 = t0**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))