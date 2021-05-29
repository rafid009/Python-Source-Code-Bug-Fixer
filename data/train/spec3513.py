import numpy as np 

def function(x):

	l1 = x
	w7 = x
	paths = []
	try:
		if l1 >= 7:
			l1 = l1/l1
			l1 = l1/5
			x = 0*7
			paths.append(1)
		else:
			x = w7-3
			x = x*4
			x = x*l1
			paths.append(2)
		if l1 >= 2:
			w7 = 6+w7
			paths.append(3)
		else:
			w7 = w7/w7
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))