import numpy as np 

def function(x):

	y5 = x
	s5 = x
	paths = []
	try:
		if s5 <= 7:
			y5 = 4*y5
			s5 = s5+5
			y5 = y5/6
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x <= 1:
			x = x*4
			paths.append(3)
		else:
			y5 = y5*x
			s5 = s5-s5
			x = 8+1
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