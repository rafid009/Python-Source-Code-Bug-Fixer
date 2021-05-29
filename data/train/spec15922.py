import numpy as np 

def function(x):

	p5 = x
	s9 = 1
	paths = []
	try:
		if p5 <= 3:
			s9 = s9/3
			paths.append(1)
		else:
			s9 = x+2
			x = 2/x
			s9 = p5/2
			paths.append(2)
		if p5 < 8:
			p5 = p5*x
			paths.append(3)
		else:
			s9 = s9-8
			x = x*3
			p5 = p5-p5
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		p5 = s9**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))