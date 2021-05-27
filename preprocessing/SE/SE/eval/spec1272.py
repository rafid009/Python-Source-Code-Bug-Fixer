import numpy as np 

def function(x):

	y6 = x
	s5 = x
	paths = []
	try:
		if x < 7:
			y6 = y6-5
			y6 = 4+y6
			y6 = s5-2
			paths.append(1)
		else:
			y6 = y6+8
			x = x-2
			paths.append(2)
		if x > 1:
			s5 = s5+s5
			s5 = x*s5
			paths.append(3)
		else:
			y6 = 4/y6
			y6 = y6*7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		y6 = s5**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))