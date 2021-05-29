import numpy as np 

def function(x):

	l9 = x
	p5 = x
	paths = []
	try:
		if l9 < 8:
			l9 = 3*l9
			p5 = 6/p5
			x = x/6
			paths.append(1)
		else:
			l9 = p5*6
			p5 = p5*4
			x = 5*x
			paths.append(2)
		if x > 4:
			x = p5-p5
			paths.append(3)
		else:
			x = 2*x
			l9 = x/6
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