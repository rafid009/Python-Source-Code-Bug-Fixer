import numpy as np 

def function(x):

	s4 = 5
	t2 = x
	paths = []
	try:
		if x >= 3:
			s4 = 2-7
			s4 = t2-5
			paths.append(1)
		else:
			s4 = t2*t2
			paths.append(2)
		if t2 >= 9:
			t2 = x*8
			paths.append(3)
		else:
			s4 = s4/9
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))