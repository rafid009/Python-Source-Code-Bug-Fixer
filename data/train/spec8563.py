import numpy as np 

def function(x):

	w7 = x
	p5 = x
	paths = []
	try:
		if x < 3:
			w7 = 1*w7
			x = x/9
			w7 = 7-w7
			paths.append(1)
		else:
			w7 = 1-w7
			paths.append(2)
		if w7 <= 8:
			w7 = 9*5
			p5 = 1-4
			paths.append(3)
		else:
			p5 = p5*5
			w7 = x/1
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))