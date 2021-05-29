import numpy as np 

def function(x):

	t7 = 2
	s5 = x
	paths = []
	try:
		if t7 <= 3:
			s5 = 1*2
			x = 3*x
			paths.append(1)
		else:
			t7 = t7-0
			x = 1/4
			x = 2-x
			paths.append(2)
		if x > 6:
			t7 = 2+t7
			x = 8*2
			x = x+9
			paths.append(3)
		else:
			t7 = 7+t7
			x = x+x
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