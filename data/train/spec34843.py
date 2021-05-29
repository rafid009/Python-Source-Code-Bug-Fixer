import numpy as np 

def function(x):

	p5 = x
	d7 = x
	paths = []
	try:
		if p5 < 9:
			p5 = p5+d7
			d7 = 0-d7
			x = x/1
			paths.append(1)
		else:
			d7 = d7-d7
			d7 = x+d7
			d7 = x*x
			paths.append(2)
		if p5 < 6:
			x = x-d7
			paths.append(3)
		else:
			p5 = p5-8
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		p5 = d7**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))