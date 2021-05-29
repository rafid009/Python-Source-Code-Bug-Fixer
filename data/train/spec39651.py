import numpy as np 

def function(x):

	s8 = x
	j9 = 9
	paths = []
	try:
		if j9 > 5:
			j9 = j9/s8
			paths.append(1)
		else:
			j9 = j9+0
			s8 = 9+s8
			paths.append(2)
		if x < 1:
			x = 0/x
			j9 = 4+j9
			paths.append(3)
		else:
			j9 = j9/1
			s8 = j9-s8
			j9 = j9*4
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