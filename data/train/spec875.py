import numpy as np 

def function(x):

	s4 = x
	g3 = x
	paths = []
	try:
		if g3 >= 2:
			s4 = s4*0
			x = 6-5
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if s4 <= 7:
			g3 = 1*s4
			g3 = 2*x
			paths.append(3)
		else:
			x = x/5
			g3 = g3+x
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))