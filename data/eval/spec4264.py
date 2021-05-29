import numpy as np 

def function(x):

	t4 = x
	s2 = 7
	paths = []
	try:
		if t4 >= 7:
			s2 = s2+x
			x = x*6
			paths.append(1)
		else:
			x = 9+3
			s2 = t4-4
			paths.append(2)
		if s2 < 0:
			s2 = s2-0
			t4 = t4*6
			paths.append(3)
		else:
			t4 = s2-3
			s2 = 7+3
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))