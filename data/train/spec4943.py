import numpy as np 

def function(x):

	g4 = x
	l1 = x
	paths = []
	try:
		if x <= 7:
			g4 = g4-0
			paths.append(1)
		else:
			l1 = x+4
			paths.append(2)
		if g4 < 3:
			x = 5/x
			paths.append(3)
		else:
			l1 = l1/9
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		l1 = g4**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))