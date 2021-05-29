import numpy as np 

def function(x):

	t3 = x
	s4 = 2
	paths = []
	try:
		if s4 > 2:
			s4 = s4*8
			t3 = 3+s4
			paths.append(1)
		else:
			x = x*s4
			paths.append(2)
		if s4 <= 3:
			s4 = 0/5
			t3 = t3+0
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		s4 = t3**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))