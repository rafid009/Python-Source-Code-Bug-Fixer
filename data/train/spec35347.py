import numpy as np 

def function(x):

	p5 = 0
	e2 = 1
	paths = []
	try:
		if e2 < 1:
			p5 = x+e2
			paths.append(1)
		else:
			e2 = e2/e2
			p5 = e2+x
			e2 = 0-8
			paths.append(2)
		if e2 > 4:
			e2 = x/4
			e2 = e2*9
			p5 = p5/6
			paths.append(3)
		else:
			p5 = x+p5
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