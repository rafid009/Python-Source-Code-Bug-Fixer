import numpy as np 

def function(x):

	v5 = 2
	s2 = 9
	paths = []
	try:
		if v5 < 5:
			x = 6-v5
			s2 = s2-1
			paths.append(1)
		else:
			x = x/6
			s2 = 0-7
			s2 = 5-s2
			paths.append(2)
		if s2 >= 6:
			x = 2-x
			v5 = x/v5
			s2 = s2*3
			paths.append(3)
		else:
			s2 = 8+s2
			x = s2*x
			v5 = 2-1
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))