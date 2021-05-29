import numpy as np 

def function(x):

	s2 = 0
	p5 = x
	paths = []
	try:
		if x <= 7:
			p5 = p5/3
			paths.append(1)
		else:
			x = x/9
			p5 = p5*1
			x = 6-x
			paths.append(2)
		if s2 > 2:
			s2 = s2*9
			paths.append(3)
		else:
			p5 = 0-p5
			x = 8-1
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		p5 = p5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))