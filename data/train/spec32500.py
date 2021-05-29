import numpy as np 

def function(x):

	s2 = 5
	g3 = x
	paths = []
	try:
		if s2 >= 1:
			g3 = g3+7
			s2 = s2*9
			paths.append(1)
		else:
			x = x/1
			s2 = 5*g3
			paths.append(2)
		if x <= 9:
			g3 = 6-g3
			paths.append(3)
		else:
			g3 = g3+x
			g3 = g3*3
			x = x*2
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		s2 = g3**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))