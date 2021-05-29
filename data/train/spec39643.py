import numpy as np 

def function(x):

	s9 = x
	g9 = 1
	paths = []
	try:
		if g9 >= 6:
			s9 = 0+s9
			s9 = s9*0
			x = x/9
			paths.append(1)
		else:
			x = 4/s9
			x = 4+g9
			paths.append(2)
		if x < 0:
			s9 = 3/s9
			g9 = 1/g9
			paths.append(3)
		else:
			g9 = g9+x
			s9 = s9*g9
			g9 = g9*g9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		g9 = s9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))