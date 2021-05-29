import numpy as np 

def function(x):

	s4 = 6
	u3 = x
	paths = []
	try:
		if s4 <= 7:
			s4 = s4/7
			x = 1+x
			u3 = u3+7
			paths.append(1)
		else:
			x = x/1
			x = x+5
			paths.append(2)
		if u3 <= 7:
			x = x-s4
			u3 = u3-7
			s4 = 4-s4
			paths.append(3)
		else:
			s4 = s4*s4
			x = 5-x
			u3 = 6+u3
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