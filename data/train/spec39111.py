import numpy as np 

def function(x):

	s7 = 2
	p5 = x
	paths = []
	try:
		if p5 > 2:
			p5 = p5-0
			paths.append(1)
		else:
			p5 = s7/p5
			s7 = 3*2
			s7 = 2-s7
			paths.append(2)
		if p5 <= 0:
			p5 = 9*0
			paths.append(3)
		else:
			x = p5-x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))