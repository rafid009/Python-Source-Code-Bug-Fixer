import numpy as np 

def function(x):

	p9 = x
	p5 = x
	paths = []
	try:
		if x < 0:
			p5 = p5/6
			x = x+6
			p9 = 3*p9
			paths.append(1)
		else:
			x = x-p5
			x = x*1
			paths.append(2)
		if p9 < 9:
			p5 = p5*8
			x = x/4
			x = x*5
			paths.append(3)
		else:
			p5 = p5*1
			p5 = 8*x
			p9 = p5/p9
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