import numpy as np 

def function(x):

	z6 = x
	p5 = x
	paths = []
	try:
		if z6 <= 3:
			x = x*z6
			paths.append(1)
		else:
			x = x+5
			x = x*7
			z6 = x/x
			paths.append(2)
		if x < 8:
			x = z6+3
			paths.append(3)
		else:
			p5 = p5-6
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