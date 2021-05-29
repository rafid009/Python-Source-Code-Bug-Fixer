import numpy as np 

def function(x):

	q9 = 6
	s8 = 9
	paths = []
	try:
		if x <= 0:
			s8 = s8/5
			q9 = x+3
			q9 = q9+4
			paths.append(1)
		else:
			s8 = q9+s8
			paths.append(2)
		if s8 > 7:
			s8 = s8-9
			x = 6+1
			s8 = s8+8
			paths.append(3)
		else:
			q9 = q9/9
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))