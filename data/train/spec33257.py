import numpy as np 

def function(x):

	g2 = 2
	s4 = 1
	paths = []
	try:
		if x <= 5:
			x = x+5
			x = 0-4
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if x >= 3:
			x = s4-x
			paths.append(3)
		else:
			s4 = 3/s4
			s4 = s4/7
			g2 = x-1
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		x = g2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))