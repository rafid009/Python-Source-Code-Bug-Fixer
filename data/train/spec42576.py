import numpy as np 

def function(x):

	o1 = 6
	p5 = 8
	paths = []
	try:
		if x >= 7:
			x = 2+3
			p5 = p5-6
			x = 6-x
			paths.append(1)
		else:
			p5 = x+2
			paths.append(2)
		if x >= 9:
			p5 = 5+o1
			p5 = 6-p5
			x = x-9
			paths.append(3)
		else:
			o1 = p5-4
			x = 4/o1
			o1 = 2*p5
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