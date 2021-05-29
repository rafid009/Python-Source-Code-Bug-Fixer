import numpy as np 

def function(x):

	n5 = x
	p5 = x
	paths = []
	try:
		if x <= 3:
			p5 = p5+p5
			paths.append(1)
		else:
			x = 1/7
			n5 = 4*n5
			x = x-2
			paths.append(2)
		if p5 > 3:
			n5 = n5-0
			n5 = 0-n5
			paths.append(3)
		else:
			p5 = p5/1
			p5 = 2+p5
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