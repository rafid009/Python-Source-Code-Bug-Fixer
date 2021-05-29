import numpy as np 

def function(x):

	p5 = x
	p8 = 5
	paths = []
	try:
		if p5 >= 0:
			x = 1+8
			paths.append(1)
		else:
			x = 9*x
			paths.append(2)
		if x > 2:
			p5 = p5+9
			p8 = x*5
			p5 = p5-p5
			paths.append(3)
		else:
			x = x/2
			x = 7/p8
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		x = p5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))