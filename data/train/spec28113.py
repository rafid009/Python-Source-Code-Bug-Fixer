import numpy as np 

def function(x):

	w7 = 1
	p1 = x
	paths = []
	try:
		if p1 > 8:
			p1 = 8*w7
			x = 2/x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x <= 7:
			x = x+3
			paths.append(3)
		else:
			w7 = w7*p1
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		w7 = p1**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))