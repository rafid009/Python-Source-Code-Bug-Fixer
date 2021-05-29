import numpy as np 

def function(x):

	s8 = 8
	n8 = x
	paths = []
	try:
		if x > 6:
			s8 = s8+0
			s8 = x/s8
			paths.append(1)
		else:
			s8 = x*s8
			s8 = 7+1
			paths.append(2)
		if n8 > 6:
			x = x/9
			paths.append(3)
		else:
			s8 = x+s8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		n8 = n8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))