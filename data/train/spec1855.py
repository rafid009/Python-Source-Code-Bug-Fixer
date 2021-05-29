import numpy as np 

def function(x):

	g5 = 3
	p5 = 6
	x = x
	paths = []
	try:
		if g5 <= 4:
			g5 = g5-1
			p5 = 2-p5
			x = x/p5
			paths.append(1)
		else:
			g5 = p5+x
			p5 = 4-p5
			x = x/x
			paths.append(2)
		if p5 <= 8:
			g5 = g5-9
			g5 = 7/9
			paths.append(3)
		else:
			x = x+1
			x = 5/p5
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		g5 = p5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))