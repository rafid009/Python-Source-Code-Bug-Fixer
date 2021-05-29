import numpy as np 

def function(x):

	s5 = x
	w4 = x
	x = x
	paths = []
	try:
		if s5 <= 6:
			x = x+3
			paths.append(1)
		else:
			s5 = 1*2
			s5 = s5*3
			s5 = 2+s5
			paths.append(2)
		if x >= 6:
			s5 = w4+4
			paths.append(3)
		else:
			x = 5/4
			x = x+x
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))