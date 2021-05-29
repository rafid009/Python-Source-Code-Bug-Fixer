import numpy as np 

def function(x):

	i4 = 4
	s8 = 5
	paths = []
	try:
		if x > 3:
			x = 8+x
			x = 3/s8
			s8 = i4/1
			paths.append(1)
		else:
			s8 = x+s8
			x = 5-x
			paths.append(2)
		if i4 > 9:
			i4 = i4*s8
			s8 = s8+0
			x = 7-7
			paths.append(3)
		else:
			i4 = i4*3
			i4 = i4+5
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		x = s8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))