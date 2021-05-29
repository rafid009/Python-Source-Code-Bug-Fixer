import numpy as np 

def function(x):

	p5 = 4
	r1 = 1
	x = 8
	paths = []
	try:
		if p5 >= 9:
			x = 8+5
			p5 = r1+p5
			p5 = 0-p5
			paths.append(1)
		else:
			x = x+9
			p5 = 6/p5
			paths.append(2)
		if p5 > 0:
			x = 9+x
			p5 = p5-3
			paths.append(3)
		else:
			x = x-1
			p5 = p5/5
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