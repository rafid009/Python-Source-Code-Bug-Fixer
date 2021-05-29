import numpy as np 

def function(x):

	p5 = 3
	i8 = 6
	paths = []
	try:
		if x <= 0:
			i8 = i8*0
			x = 4+x
			paths.append(1)
		else:
			i8 = 9+p5
			i8 = 1*6
			paths.append(2)
		if x > 8:
			i8 = 4+i8
			paths.append(3)
		else:
			p5 = i8/p5
			p5 = i8+x
			p5 = 8-9
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