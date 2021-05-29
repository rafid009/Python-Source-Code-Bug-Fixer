import numpy as np 

def function(x):

	z9 = x
	p5 = x
	paths = []
	try:
		if p5 <= 0:
			z9 = z9+x
			paths.append(1)
		else:
			x = x*z9
			paths.append(2)
		if p5 > 1:
			x = p5*x
			x = 5+x
			p5 = 6*8
			paths.append(3)
		else:
			p5 = 0*p5
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))