import numpy as np 

def function(x):

	p5 = x
	d4 = x
	paths = []
	try:
		if p5 >= 2:
			x = 0-x
			d4 = x/d4
			x = 0-d4
			paths.append(1)
		else:
			p5 = 2/p5
			d4 = 8*d4
			paths.append(2)
		if x < 7:
			d4 = d4+9
			paths.append(3)
		else:
			p5 = 9-1
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		x = p5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))