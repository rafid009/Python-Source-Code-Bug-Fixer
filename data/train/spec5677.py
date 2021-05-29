import numpy as np 

def function(x):

	o7 = 2
	p5 = x
	paths = []
	try:
		if p5 <= 3:
			o7 = 7-o7
			p5 = p5*p5
			paths.append(1)
		else:
			p5 = x+7
			paths.append(2)
		if o7 >= 5:
			x = x*6
			paths.append(3)
		else:
			o7 = 7-o7
			o7 = 4/o7
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