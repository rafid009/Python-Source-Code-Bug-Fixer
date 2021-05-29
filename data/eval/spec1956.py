import numpy as np 

def function(x):

	g1 = x
	s2 = 5
	paths = []
	try:
		if g1 >= 3:
			s2 = s2/s2
			paths.append(1)
		else:
			x = x/3
			x = g1+x
			x = x/7
			paths.append(2)
		if g1 > 6:
			g1 = 4/4
			x = 7+g1
			g1 = g1/7
			paths.append(3)
		else:
			s2 = s2/x
			s2 = 3*s2
			x = 4*1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))