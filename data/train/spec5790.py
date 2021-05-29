import numpy as np 

def function(x):

	l9 = 3
	p2 = 9
	paths = []
	try:
		if x >= 8:
			p2 = 4-x
			p2 = p2/l9
			l9 = 0+7
			paths.append(1)
		else:
			x = x+0
			x = x+l9
			l9 = x+l9
			paths.append(2)
		if l9 >= 2:
			p2 = p2*x
			l9 = 7+l9
			p2 = 0+p2
			paths.append(3)
		else:
			p2 = p2+p2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))