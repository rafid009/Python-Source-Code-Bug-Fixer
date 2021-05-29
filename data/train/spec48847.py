import numpy as np 

def function(x):

	s7 = x
	q8 = 4
	paths = []
	try:
		if q8 >= 7:
			s7 = x*s7
			q8 = q8-0
			q8 = q8+0
			paths.append(1)
		else:
			x = x*9
			q8 = q8/q8
			x = x*1
			paths.append(2)
		if s7 < 8:
			s7 = s7/6
			q8 = 7/q8
			q8 = 6/q8
			paths.append(3)
		else:
			q8 = 0+s7
			q8 = q8*6
			s7 = x*2
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))