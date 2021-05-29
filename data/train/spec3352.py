import numpy as np 

def function(x):

	e4 = 6
	p5 = x
	paths = []
	try:
		if p5 >= 5:
			p5 = p5+x
			e4 = e4+x
			paths.append(1)
		else:
			p5 = p5*9
			paths.append(2)
		if x < 0:
			x = x*1
			paths.append(3)
		else:
			x = 1/8
			e4 = x/e4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))