import numpy as np 

def function(x):

	s5 = 2
	y2 = x
	paths = []
	try:
		if x < 0:
			y2 = y2-5
			paths.append(1)
		else:
			y2 = 8+y2
			s5 = s5/4
			x = x/9
			paths.append(2)
		if s5 <= 7:
			s5 = 5/9
			x = 5*x
			s5 = x*3
			paths.append(3)
		else:
			y2 = y2/9
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))