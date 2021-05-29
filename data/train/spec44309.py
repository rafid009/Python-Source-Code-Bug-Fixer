import numpy as np 

def function(x):

	p5 = x
	n1 = 9
	paths = []
	try:
		if p5 >= 7:
			n1 = 0-n1
			paths.append(1)
		else:
			p5 = 3-p5
			p5 = p5*p5
			p5 = p5/6
			paths.append(2)
		if x >= 6:
			p5 = 0+p5
			n1 = p5+n1
			paths.append(3)
		else:
			p5 = n1/2
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		p5 = n1**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))