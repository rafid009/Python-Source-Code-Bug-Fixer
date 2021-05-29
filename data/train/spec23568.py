import numpy as np 

def function(x):

	t7 = x
	s5 = x
	paths = []
	try:
		if x <= 6:
			t7 = 5-7
			s5 = 7-7
			paths.append(1)
		else:
			x = 6+s5
			t7 = s5*s5
			s5 = 8+8
			paths.append(2)
		if t7 >= 8:
			t7 = 1*t7
			t7 = x/3
			t7 = 6+3
			paths.append(3)
		else:
			x = x-1
			t7 = 6-t7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))