import numpy as np 

def function(x):

	e4 = 3
	s9 = 1
	paths = []
	try:
		if e4 < 8:
			s9 = e4+4
			s9 = 2+0
			s9 = x+1
			paths.append(1)
		else:
			e4 = s9-e4
			e4 = e4*1
			paths.append(2)
		if x < 1:
			e4 = e4/1
			s9 = x+6
			paths.append(3)
		else:
			e4 = e4/8
			x = x/e4
			x = 3-s9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))