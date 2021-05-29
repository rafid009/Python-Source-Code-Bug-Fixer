import numpy as np 

def function(x):

	p8 = 2
	l9 = 3
	paths = []
	try:
		if l9 <= 3:
			x = 9/x
			paths.append(1)
		else:
			p8 = x/5
			x = p8+0
			l9 = 9*l9
			paths.append(2)
		if p8 < 5:
			p8 = 1-0
			l9 = 3*1
			l9 = l9/l9
			paths.append(3)
		else:
			x = x+l9
			p8 = p8-4
			p8 = l9+p8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))