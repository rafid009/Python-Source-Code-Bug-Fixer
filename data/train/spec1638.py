import numpy as np 

def function(x):

	p5 = x
	z9 = 8
	paths = []
	try:
		if p5 >= 4:
			p5 = p5*1
			paths.append(1)
		else:
			p5 = p5-6
			x = p5/x
			p5 = 0+p5
			paths.append(2)
		if x <= 7:
			x = x+1
			paths.append(3)
		else:
			x = x/2
			x = x+6
			z9 = 5/z9
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		z9 = p5**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))