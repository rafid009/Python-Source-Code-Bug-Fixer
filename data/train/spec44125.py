import numpy as np 

def function(x):

	s0 = x
	y2 = x
	paths = []
	try:
		if y2 > 0:
			y2 = x/y2
			paths.append(1)
		else:
			s0 = 5*0
			s0 = s0+1
			paths.append(2)
		if x <= 5:
			y2 = y2+5
			s0 = s0/s0
			paths.append(3)
		else:
			x = 2+x
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