import numpy as np 

def function(x):

	p5 = 0
	i8 = x
	x = x
	paths = []
	try:
		if p5 < 8:
			i8 = 8+0
			paths.append(1)
		else:
			x = x*p5
			p5 = 1+0
			paths.append(2)
		if p5 <= 5:
			i8 = i8-0
			p5 = p5*4
			x = i8-x
			paths.append(3)
		else:
			i8 = 2-i8
			x = x/5
			i8 = p5+4
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