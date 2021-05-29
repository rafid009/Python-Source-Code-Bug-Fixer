import numpy as np 

def function(x):

	d1 = 4
	p5 = 1
	paths = []
	try:
		if x <= 4:
			p5 = p5-3
			p5 = p5*2
			paths.append(1)
		else:
			p5 = p5*7
			d1 = x+d1
			paths.append(2)
		if p5 < 6:
			x = x-7
			paths.append(3)
		else:
			d1 = 1-d1
			p5 = x+p5
			x = p5/x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))