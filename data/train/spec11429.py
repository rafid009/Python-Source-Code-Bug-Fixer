import numpy as np 

def function(x):

	c2 = x
	s5 = 9
	paths = []
	try:
		if s5 < 0:
			x = s5+6
			s5 = s5/x
			paths.append(1)
		else:
			c2 = c2/8
			paths.append(2)
		if x < 6:
			s5 = 8/s5
			s5 = s5*1
			paths.append(3)
		else:
			x = x/5
			c2 = c2-2
			s5 = c2-s5
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))