import numpy as np 

def function(x):

	s7 = x
	g9 = 3
	paths = []
	try:
		if s7 > 1:
			g9 = 7+9
			x = x/1
			paths.append(1)
		else:
			x = x-g9
			g9 = s7*g9
			s7 = s7+6
			paths.append(2)
		if x > 4:
			x = 4/3
			s7 = 2-4
			paths.append(3)
		else:
			g9 = 7/s7
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))