import numpy as np 

def function(x):

	p5 = 4
	n0 = x
	paths = []
	try:
		if x <= 4:
			x = x/x
			n0 = 8*n0
			p5 = 4+p5
			paths.append(1)
		else:
			n0 = 1*x
			n0 = n0/n0
			paths.append(2)
		if n0 >= 1:
			p5 = x/7
			p5 = 2+5
			x = 2-x
			paths.append(3)
		else:
			p5 = 0+p5
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		p5 = n0**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))