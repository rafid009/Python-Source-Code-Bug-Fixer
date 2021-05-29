import numpy as np 

def function(x):

	p5 = x
	s4 = 8
	x = x
	paths = []
	try:
		if x > 6:
			x = 3/2
			paths.append(1)
		else:
			x = s4/8
			s4 = s4-0
			paths.append(2)
		if x >= 4:
			p5 = p5/9
			p5 = s4*p5
			x = 7-9
			paths.append(3)
		else:
			x = 7*s4
			p5 = 7*p5
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		s4 = p5**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))