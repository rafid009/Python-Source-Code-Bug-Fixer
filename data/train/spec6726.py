import numpy as np 

def function(x):

	s1 = 9
	g3 = x
	paths = []
	try:
		if g3 <= 7:
			x = 1/7
			g3 = g3+5
			s1 = 6+s1
			paths.append(1)
		else:
			g3 = 2-6
			g3 = g3*4
			paths.append(2)
		if x < 5:
			x = g3-g3
			x = 7+x
			paths.append(3)
		else:
			s1 = x*8
			x = 4-x
			s1 = s1*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))