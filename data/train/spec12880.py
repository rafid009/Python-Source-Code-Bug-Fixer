import numpy as np 

def function(x):

	p1 = 4
	w9 = x
	x = 5
	paths = []
	try:
		if x >= 0:
			p1 = 3*4
			x = 7/w9
			paths.append(1)
		else:
			x = x*x
			p1 = 0/1
			x = 3-7
			paths.append(2)
		if w9 >= 1:
			x = w9-x
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w9 = w9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))