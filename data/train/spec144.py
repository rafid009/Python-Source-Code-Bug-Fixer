import numpy as np 

def function(x):

	p5 = x
	p6 = 3
	paths = []
	try:
		if x < 6:
			x = p5*1
			paths.append(1)
		else:
			p5 = p5*8
			p6 = 0+9
			paths.append(2)
		if p5 <= 8:
			x = x+p6
			p5 = p5/7
			paths.append(3)
		else:
			p6 = 4/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))