import numpy as np 

def function(x):

	p5 = x
	g4 = 9
	x = 4
	paths = []
	try:
		if p5 > 3:
			x = 0-9
			x = x*x
			paths.append(1)
		else:
			x = g4-9
			x = 0-1
			x = g4+x
			paths.append(2)
		if g4 <= 8:
			x = x*g4
			paths.append(3)
		else:
			p5 = p5/3
			x = x-g4
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		p5 = p5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))