import numpy as np 

def function(x):

	v4 = x
	s9 = x
	paths = []
	try:
		if x <= 5:
			v4 = v4*5
			s9 = 6/s9
			x = 4-8
			paths.append(1)
		else:
			x = 9+x
			s9 = s9/7
			paths.append(2)
		if s9 >= 7:
			s9 = 7+7
			paths.append(3)
		else:
			v4 = v4+v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))