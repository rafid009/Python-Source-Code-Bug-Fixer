import numpy as np 

def function(x):

	w4 = 7
	p1 = 2
	paths = []
	try:
		if w4 <= 0:
			w4 = 2-1
			paths.append(1)
		else:
			x = 2/x
			p1 = 7/p1
			p1 = p1-4
			paths.append(2)
		if p1 >= 3:
			x = x*9
			p1 = w4+w4
			paths.append(3)
		else:
			x = x+0
			x = 6-w4
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		w4 = p1**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))