import numpy as np 

def function(x):

	l4 = 8
	d7 = 6
	paths = []
	try:
		if l4 <= 9:
			d7 = 4-0
			d7 = d7/3
			d7 = x*l4
			paths.append(1)
		else:
			x = l4*5
			paths.append(2)
		if l4 < 7:
			x = x/l4
			x = 9*x
			paths.append(3)
		else:
			x = 2+6
			l4 = l4/7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		l4 = d7**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))