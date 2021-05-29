import numpy as np 

def function(x):

	p5 = 2
	b5 = x
	paths = []
	try:
		if b5 >= 2:
			b5 = b5+6
			paths.append(1)
		else:
			b5 = b5+0
			paths.append(2)
		if x > 1:
			p5 = 3+p5
			p5 = p5-2
			b5 = b5*b5
			paths.append(3)
		else:
			p5 = 3*p5
			x = x/2
			p5 = 7/x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))