import numpy as np 

def function(x):

	s4 = x
	p5 = x
	paths = []
	try:
		if x < 0:
			p5 = p5*3
			paths.append(1)
		else:
			p5 = p5-x
			x = x-7
			s4 = x/8
			paths.append(2)
		if x <= 2:
			x = x*9
			s4 = p5+x
			paths.append(3)
		else:
			x = x+x
			s4 = s4/5
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p5 = x**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))