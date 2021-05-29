import numpy as np 

def function(x):

	a5 = x
	s1 = 2
	paths = []
	try:
		if x <= 5:
			s1 = a5+8
			a5 = a5/a5
			paths.append(1)
		else:
			a5 = a5-7
			x = x/8
			paths.append(2)
		if x >= 3:
			x = s1/8
			a5 = x*9
			s1 = a5*5
			paths.append(3)
		else:
			x = x+7
			a5 = s1/a5
			x = x/5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		s1 = a5**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))