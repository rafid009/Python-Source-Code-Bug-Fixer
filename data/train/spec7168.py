import numpy as np 

def function(x):

	p5 = 7
	o5 = 9
	paths = []
	try:
		if x < 8:
			p5 = p5/x
			paths.append(1)
		else:
			o5 = p5/p5
			x = 5*x
			p5 = o5/o5
			paths.append(2)
		if o5 < 0:
			o5 = o5-x
			x = x*7
			paths.append(3)
		else:
			x = x-p5
			x = x+3
			p5 = p5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))