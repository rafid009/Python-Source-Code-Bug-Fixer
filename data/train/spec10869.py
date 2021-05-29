import numpy as np 

def function(x):

	p5 = 7
	i6 = 4
	paths = []
	try:
		if x <= 9:
			x = x+p5
			i6 = i6/1
			paths.append(1)
		else:
			x = 9/1
			x = 4*3
			paths.append(2)
		if x < 0:
			i6 = 6-p5
			p5 = p5+3
			i6 = 9-i6
			paths.append(3)
		else:
			p5 = p5-p5
			i6 = i6+p5
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