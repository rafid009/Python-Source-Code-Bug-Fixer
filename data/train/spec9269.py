import numpy as np 

def function(x):

	t7 = x
	s4 = x
	paths = []
	try:
		if s4 >= 1:
			x = 5/x
			s4 = s4/3
			paths.append(1)
		else:
			x = x*8
			x = x+t7
			x = t7*x
			paths.append(2)
		if t7 > 2:
			x = x/5
			x = x+2
			paths.append(3)
		else:
			s4 = 3+s4
			t7 = t7+x
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))