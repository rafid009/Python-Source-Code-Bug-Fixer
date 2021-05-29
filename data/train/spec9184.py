import numpy as np 

def function(x):

	s6 = 0
	g2 = 0
	paths = []
	try:
		if s6 <= 3:
			s6 = s6+s6
			s6 = 1+x
			x = x*1
			paths.append(1)
		else:
			x = 0-s6
			s6 = s6/5
			paths.append(2)
		if s6 > 4:
			x = 9+4
			s6 = s6+8
			x = 1/s6
			paths.append(3)
		else:
			g2 = g2/2
			g2 = g2-2
			g2 = g2/5
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