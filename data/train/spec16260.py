import numpy as np 

def function(x):

	x2 = x
	p5 = x
	paths = []
	try:
		if p5 < 8:
			x = x*x2
			x = x2*x2
			paths.append(1)
		else:
			x = x+3
			p5 = x-x
			x2 = x2-2
			paths.append(2)
		if x2 >= 4:
			p5 = p5+6
			x = x+8
			paths.append(3)
		else:
			x = 4-p5
			x = 9-x
			x2 = x2-9
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		x2 = p5**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))