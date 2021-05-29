import numpy as np 

def function(x):

	p1 = x
	p5 = x
	paths = []
	try:
		if p5 >= 7:
			p1 = p1*9
			paths.append(1)
		else:
			p5 = 6-p5
			p1 = p1*p1
			paths.append(2)
		if p5 >= 3:
			p5 = p5+4
			p5 = 8-p5
			p5 = p1-p5
			paths.append(3)
		else:
			x = p1*x
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