import numpy as np 

def function(x):

	s8 = x
	j2 = 0
	paths = []
	try:
		if s8 <= 1:
			j2 = j2*3
			s8 = 5*6
			x = 4-x
			paths.append(1)
		else:
			s8 = 7-s8
			paths.append(2)
		if s8 <= 3:
			x = 8-x
			x = x*8
			paths.append(3)
		else:
			s8 = x/3
			s8 = j2/s8
			x = x+5
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		j2 = s8**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))