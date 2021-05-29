import numpy as np 

def function(x):

	p5 = x
	b8 = 3
	x = x
	paths = []
	try:
		if b8 >= 8:
			b8 = b8/b8
			x = 4/x
			paths.append(1)
		else:
			b8 = p5*b8
			p5 = p5*8
			paths.append(2)
		if b8 >= 6:
			x = 8-x
			x = x/p5
			b8 = 5*p5
			paths.append(3)
		else:
			x = x-p5
			x = 8+9
			x = x-9
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		p5 = b8**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))