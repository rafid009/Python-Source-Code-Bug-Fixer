import numpy as np 

def function(x):

	p9 = x
	s2 = 1
	paths = []
	try:
		if x > 5:
			p9 = 9+x
			p9 = 2+p9
			paths.append(1)
		else:
			x = 5+4
			p9 = 1-p9
			x = p9+s2
			paths.append(2)
		if x >= 9:
			p9 = 2*0
			s2 = 1/s2
			p9 = s2-x
			paths.append(3)
		else:
			x = x*8
			s2 = p9/s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))