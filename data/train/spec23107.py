import numpy as np 

def function(x):

	z7 = x
	p5 = 1
	x = x
	paths = []
	try:
		if x <= 1:
			p5 = p5*p5
			paths.append(1)
		else:
			x = x*8
			x = 0+x
			p5 = p5/4
			paths.append(2)
		if p5 > 4:
			p5 = 5-x
			z7 = 5*z7
			paths.append(3)
		else:
			p5 = p5-p5
			p5 = 3+p5
			p5 = 0-p5
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