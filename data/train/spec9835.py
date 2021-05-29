import numpy as np 

def function(x):

	v6 = 2
	s5 = x
	paths = []
	try:
		if x <= 9:
			s5 = s5-2
			v6 = v6/s5
			x = x/9
			paths.append(1)
		else:
			v6 = x/8
			s5 = 9*s5
			s5 = s5/1
			paths.append(2)
		if s5 < 0:
			v6 = 0+v6
			paths.append(3)
		else:
			s5 = 6/s5
			s5 = 2*s5
			x = x-x
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