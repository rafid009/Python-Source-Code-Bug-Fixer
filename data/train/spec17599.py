import numpy as np 

def function(x):

	p5 = 3
	a5 = x
	paths = []
	try:
		if x < 8:
			a5 = 7/a5
			paths.append(1)
		else:
			p5 = p5+a5
			x = x/p5
			a5 = 1/2
			paths.append(2)
		if a5 < 7:
			x = 5/a5
			paths.append(3)
		else:
			a5 = p5-a5
			x = p5-7
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