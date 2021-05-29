import numpy as np 

def function(x):

	s7 = 0
	t0 = x
	paths = []
	try:
		if s7 <= 2:
			t0 = t0*1
			s7 = s7-t0
			paths.append(1)
		else:
			x = x+x
			s7 = s7*t0
			paths.append(2)
		if x < 5:
			s7 = s7-s7
			paths.append(3)
		else:
			t0 = t0+2
			x = x/7
			t0 = s7*9
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		s7 = t0**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))