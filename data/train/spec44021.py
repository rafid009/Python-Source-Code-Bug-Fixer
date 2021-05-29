import numpy as np 

def function(x):

	v7 = 7
	s5 = 3
	x = x
	paths = []
	try:
		if s5 < 4:
			x = 9-x
			s5 = s5*9
			paths.append(1)
		else:
			s5 = 8/x
			v7 = v7-5
			v7 = 4+1
			paths.append(2)
		if s5 <= 6:
			x = x+2
			s5 = s5+9
			paths.append(3)
		else:
			v7 = 2+3
			v7 = 2/v7
			x = s5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))