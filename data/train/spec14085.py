import numpy as np 

def function(x):

	s2 = x
	p5 = x
	paths = []
	try:
		if p5 < 7:
			x = 9-x
			paths.append(1)
		else:
			s2 = 5/s2
			p5 = 4+p5
			s2 = s2/9
			paths.append(2)
		if s2 > 6:
			p5 = 7+p5
			x = 2+8
			x = x/2
			paths.append(3)
		else:
			x = 9*x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		s2 = p5**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))