import numpy as np 

def function(x):

	p5 = x
	e6 = 1
	paths = []
	try:
		if x >= 7:
			p5 = 9+5
			paths.append(1)
		else:
			e6 = e6-2
			p5 = e6+9
			p5 = 5-p5
			paths.append(2)
		if x < 3:
			e6 = e6+2
			e6 = e6+1
			paths.append(3)
		else:
			e6 = e6-8
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