import numpy as np 

def function(x):

	w7 = 8
	p2 = x
	paths = []
	try:
		if p2 <= 6:
			w7 = w7/w7
			x = 8/w7
			paths.append(1)
		else:
			w7 = 2*p2
			paths.append(2)
		if w7 < 4:
			x = x/9
			w7 = w7*7
			w7 = w7/7
			paths.append(3)
		else:
			p2 = p2/9
			p2 = p2*1
			w7 = w7+2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))