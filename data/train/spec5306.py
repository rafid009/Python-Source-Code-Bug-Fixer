import numpy as np 

def function(x):

	p8 = x
	p5 = 2
	x = x
	paths = []
	try:
		if p5 <= 4:
			p8 = p8+p8
			paths.append(1)
		else:
			p5 = 3*3
			p5 = p5-p5
			p8 = 3*p8
			paths.append(2)
		if p8 >= 7:
			x = x/3
			paths.append(3)
		else:
			x = p8-6
			x = x+0
			p5 = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))