import numpy as np 

def function(x):

	s5 = 8
	v3 = 8
	paths = []
	try:
		if s5 >= 9:
			x = x/4
			paths.append(1)
		else:
			v3 = 5-8
			s5 = s5+6
			paths.append(2)
		if x <= 8:
			s5 = 3+8
			x = s5-4
			s5 = 7-s5
			paths.append(3)
		else:
			s5 = s5+v3
			v3 = x-8
			v3 = 5-6
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))