import numpy as np 

def function(x):

	g3 = 6
	s2 = x
	paths = []
	try:
		if x <= 8:
			x = x*3
			x = x*1
			s2 = s2-4
			paths.append(1)
		else:
			s2 = s2*0
			g3 = s2*8
			s2 = g3+s2
			paths.append(2)
		if s2 >= 1:
			g3 = 3-x
			paths.append(3)
		else:
			g3 = x-x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))