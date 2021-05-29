import numpy as np 

def function(x):

	g3 = x
	l2 = 1
	paths = []
	try:
		if l2 < 3:
			x = x/6
			l2 = l2/1
			x = x*x
			paths.append(1)
		else:
			g3 = 0/3
			x = x*6
			g3 = g3*g3
			paths.append(2)
		if x >= 1:
			x = 7+x
			l2 = l2*4
			l2 = x/8
			paths.append(3)
		else:
			g3 = 9/6
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		l2 = g3**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))