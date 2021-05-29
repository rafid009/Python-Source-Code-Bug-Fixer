import numpy as np 

def function(x):

	x5 = 0
	p5 = 2
	paths = []
	try:
		if x5 <= 7:
			x5 = x+x
			x5 = 7+x5
			paths.append(1)
		else:
			p5 = p5/5
			paths.append(2)
		if x > 3:
			x = 3*x
			paths.append(3)
		else:
			x5 = x5*5
			p5 = 2-7
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		p5 = x5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))