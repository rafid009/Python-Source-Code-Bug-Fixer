import numpy as np 

def function(x):

	p5 = 0
	p1 = 6
	paths = []
	try:
		if p5 >= 1:
			x = p1-1
			p1 = p1/x
			paths.append(1)
		else:
			p5 = p1-x
			p5 = p5/6
			p5 = 8+3
			paths.append(2)
		if p5 >= 0:
			x = x*p1
			paths.append(3)
		else:
			p1 = 6+2
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