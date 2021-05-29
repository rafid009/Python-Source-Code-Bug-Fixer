import numpy as np 

def function(x):

	p5 = 8
	b2 = 4
	paths = []
	try:
		if x >= 9:
			b2 = b2/7
			p5 = p5+x
			paths.append(1)
		else:
			b2 = 3/x
			p5 = 3*b2
			b2 = b2+8
			paths.append(2)
		if p5 >= 2:
			x = 5/x
			p5 = b2-b2
			paths.append(3)
		else:
			p5 = p5-7
			x = x*b2
			x = x*5
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