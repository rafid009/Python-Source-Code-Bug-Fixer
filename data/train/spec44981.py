import numpy as np 

def function(x):

	b8 = x
	p5 = 7
	paths = []
	try:
		if b8 > 2:
			b8 = b8-6
			p5 = p5+p5
			b8 = b8/6
			paths.append(1)
		else:
			x = x*8
			p5 = b8+2
			paths.append(2)
		if x <= 6:
			x = x+5
			x = x-0
			paths.append(3)
		else:
			x = b8-x
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