import numpy as np 

def function(x):

	s5 = 2
	a5 = 7
	paths = []
	try:
		if x < 6:
			a5 = 0/s5
			a5 = a5+a5
			a5 = 9/4
			paths.append(1)
		else:
			s5 = s5-6
			paths.append(2)
		if s5 <= 5:
			a5 = 3*a5
			s5 = s5-9
			paths.append(3)
		else:
			x = 4+x
			s5 = s5-6
			s5 = 5+a5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))