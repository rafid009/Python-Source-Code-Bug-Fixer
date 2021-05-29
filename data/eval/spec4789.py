import numpy as np 

def function(x):

	s1 = x
	g5 = 6
	paths = []
	try:
		if g5 <= 9:
			g5 = 6-g5
			s1 = x+7
			paths.append(1)
		else:
			x = x*g5
			s1 = s1-2
			paths.append(2)
		if g5 >= 7:
			g5 = g5/9
			paths.append(3)
		else:
			s1 = 4/s1
			x = x/6
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