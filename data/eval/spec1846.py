import numpy as np 

def function(x):

	y6 = x
	s2 = x
	paths = []
	try:
		if x > 5:
			x = x*3
			x = x+7
			paths.append(1)
		else:
			x = x*x
			x = s2/8
			y6 = y6*8
			paths.append(2)
		if x >= 7:
			y6 = x/5
			s2 = 4+s2
			paths.append(3)
		else:
			y6 = 4+y6
			s2 = s2-6
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))