import numpy as np 

def function(x):

	n9 = x
	p5 = x
	paths = []
	try:
		if p5 >= 3:
			x = p5*4
			p5 = 2/p5
			p5 = p5*9
			paths.append(1)
		else:
			n9 = x/5
			p5 = p5-4
			x = x+0
			paths.append(2)
		if n9 > 8:
			p5 = x-n9
			paths.append(3)
		else:
			x = 3*x
			p5 = 9+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))