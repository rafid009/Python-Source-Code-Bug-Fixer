import numpy as np 

def function(x):

	p5 = 7
	a8 = x
	paths = []
	try:
		if p5 >= 0:
			a8 = a8+a8
			a8 = 1+a8
			a8 = 9-a8
			paths.append(1)
		else:
			p5 = 6*p5
			paths.append(2)
		if a8 > 8:
			x = p5-0
			p5 = p5-a8
			p5 = p5/9
			paths.append(3)
		else:
			a8 = a8+0
			p5 = x+p5
			x = x/4
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))