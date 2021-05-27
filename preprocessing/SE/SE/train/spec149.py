import numpy as np 

def function(x):

	s9 = x
	g9 = x
	paths = []
	try:
		if x >= 0:
			s9 = 6/8
			paths.append(1)
		else:
			x = 0+g9
			x = g9+x
			paths.append(2)
		if x > 2:
			g9 = x/g9
			x = x+s9
			g9 = 7+9
			paths.append(3)
		else:
			g9 = 9/g9
			g9 = x*s9
			g9 = g9/1
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))