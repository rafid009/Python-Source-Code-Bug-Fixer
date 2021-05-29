import numpy as np 

def function(x):

	y6 = 7
	s9 = x
	x = 3
	paths = []
	try:
		if y6 >= 7:
			x = x/3
			paths.append(1)
		else:
			y6 = 4/y6
			x = x*3
			s9 = s9*1
			paths.append(2)
		if s9 > 7:
			s9 = 1-9
			y6 = s9*3
			paths.append(3)
		else:
			x = x*8
			y6 = 5/s9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		y6 = s9**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))