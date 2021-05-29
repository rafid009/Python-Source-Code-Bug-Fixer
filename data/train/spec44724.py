import numpy as np 

def function(x):

	p6 = x
	p5 = x
	paths = []
	try:
		if p5 < 0:
			p5 = p6/x
			p6 = p6+8
			paths.append(1)
		else:
			x = p6*p6
			p5 = 4*5
			paths.append(2)
		if p5 >= 2:
			p6 = 9/p6
			p5 = 1+p5
			p6 = p6-x
			paths.append(3)
		else:
			p5 = 7*p5
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))