import numpy as np 

def function(x):

	a6 = x
	p5 = 5
	paths = []
	try:
		if a6 >= 4:
			a6 = 5*1
			paths.append(1)
		else:
			p5 = x/4
			p5 = 6/p5
			x = x-4
			paths.append(2)
		if p5 > 1:
			p5 = x+x
			x = a6+p5
			paths.append(3)
		else:
			p5 = p5-a6
			a6 = 4-3
			a6 = a6+2
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