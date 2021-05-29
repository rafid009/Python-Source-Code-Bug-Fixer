import numpy as np 

def function(x):

	p5 = 3
	l6 = 9
	paths = []
	try:
		if x > 2:
			l6 = x+3
			p5 = 9*2
			paths.append(1)
		else:
			p5 = l6/p5
			x = 2*4
			paths.append(2)
		if x < 0:
			x = p5/p5
			x = x*3
			l6 = 4*l6
			paths.append(3)
		else:
			l6 = x*4
			l6 = x-3
			p5 = l6-7
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))