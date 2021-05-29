import numpy as np 

def function(x):

	a5 = x
	p5 = x
	paths = []
	try:
		if a5 > 5:
			p5 = 6-p5
			a5 = a5*7
			p5 = p5*9
			paths.append(1)
		else:
			p5 = p5-p5
			paths.append(2)
		if p5 > 1:
			p5 = 2+p5
			a5 = 8*a5
			x = 6*x
			paths.append(3)
		else:
			p5 = p5/9
			a5 = p5+p5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))