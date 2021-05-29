import numpy as np 

def function(x):

	p5 = x
	e7 = x
	paths = []
	try:
		if p5 >= 5:
			e7 = e7-e7
			paths.append(1)
		else:
			e7 = e7+p5
			e7 = e7-5
			x = x*4
			paths.append(2)
		if e7 >= 0:
			e7 = 8/7
			paths.append(3)
		else:
			e7 = 9-e7
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