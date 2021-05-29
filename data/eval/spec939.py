import numpy as np 

def function(x):

	d5 = x
	s7 = 7
	paths = []
	try:
		if x > 4:
			x = x+s7
			x = 0/d5
			paths.append(1)
		else:
			s7 = s7-4
			s7 = s7-d5
			paths.append(2)
		if d5 >= 0:
			s7 = x/1
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))