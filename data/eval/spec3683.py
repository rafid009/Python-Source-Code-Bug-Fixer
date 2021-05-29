import numpy as np 

def function(x):

	s8 = x
	n8 = x
	paths = []
	try:
		if n8 > 9:
			x = x-0
			n8 = x/4
			n8 = n8/5
			paths.append(1)
		else:
			x = 6-s8
			paths.append(2)
		if x <= 2:
			n8 = n8+1
			x = s8*6
			paths.append(3)
		else:
			n8 = s8+3
			x = x+6
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))