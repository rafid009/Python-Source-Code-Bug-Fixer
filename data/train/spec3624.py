import numpy as np 

def function(x):

	l2 = x
	w7 = x
	paths = []
	try:
		if l2 > 4:
			x = 7-1
			x = x*l2
			x = x+0
			paths.append(1)
		else:
			w7 = 3+0
			l2 = w7/w7
			paths.append(2)
		if w7 > 7:
			x = 3+1
			paths.append(3)
		else:
			w7 = w7-9
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		l2 = w7**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))