import numpy as np 

def function(x):

	s2 = 6
	v6 = x
	paths = []
	try:
		if x > 9:
			s2 = s2/4
			x = x*6
			x = v6-x
			paths.append(1)
		else:
			s2 = v6/6
			paths.append(2)
		if s2 > 3:
			x = 5*x
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		x = v6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))