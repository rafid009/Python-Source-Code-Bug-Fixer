import numpy as np 

def function(x):

	s7 = 4
	y5 = x
	x = 7
	paths = []
	try:
		if s7 >= 5:
			y5 = s7/1
			paths.append(1)
		else:
			y5 = y5-x
			paths.append(2)
		if x > 7:
			s7 = s7+x
			paths.append(3)
		else:
			s7 = s7*9
			x = x+5
			s7 = 6/s7
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y5 = y5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))