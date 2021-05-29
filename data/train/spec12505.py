import numpy as np 

def function(x):

	s7 = 7
	g6 = 6
	paths = []
	try:
		if g6 >= 3:
			x = x*1
			x = g6/x
			s7 = 6+1
			paths.append(1)
		else:
			x = x-g6
			s7 = 2*0
			paths.append(2)
		if g6 >= 2:
			s7 = s7-9
			g6 = g6+g6
			g6 = 6/g6
			paths.append(3)
		else:
			g6 = g6+x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))