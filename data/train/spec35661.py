import numpy as np 

def function(x):

	x1 = x
	p5 = 6
	paths = []
	try:
		if x1 >= 7:
			x1 = x1+x
			p5 = 1*p5
			p5 = p5+3
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if x1 <= 2:
			x = x-4
			p5 = p5/p5
			paths.append(3)
		else:
			x = p5+4
			p5 = 9+p5
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))