import numpy as np 

def function(x):

	m3 = 6
	s2 = 2
	paths = []
	try:
		if x > 9:
			s2 = 0*3
			x = 6*m3
			x = x/x
			paths.append(1)
		else:
			s2 = s2/x
			m3 = 9*m3
			paths.append(2)
		if x < 2:
			s2 = m3*7
			s2 = 9-s2
			s2 = 7+s2
			paths.append(3)
		else:
			s2 = s2*5
			x = x*0
			x = 8+x
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