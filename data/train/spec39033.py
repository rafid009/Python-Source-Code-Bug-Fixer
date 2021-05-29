import numpy as np 

def function(x):

	p5 = 6
	l1 = 8
	paths = []
	try:
		if l1 >= 8:
			x = 7-x
			l1 = x+5
			l1 = l1-5
			paths.append(1)
		else:
			p5 = 0+9
			paths.append(2)
		if p5 < 6:
			p5 = 6/p5
			p5 = 3*p5
			paths.append(3)
		else:
			p5 = p5/1
			p5 = p5-7
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