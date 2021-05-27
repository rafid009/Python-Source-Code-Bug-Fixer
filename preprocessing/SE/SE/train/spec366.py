import numpy as np 

def function(x):

	l5 = 1
	d5 = x
	paths = []
	try:
		if x <= 9:
			d5 = d5*x
			paths.append(1)
		else:
			d5 = 4-d5
			x = 5/l5
			l5 = d5-7
			paths.append(2)
		if l5 > 7:
			d5 = d5-l5
			l5 = l5+x
			paths.append(3)
		else:
			l5 = 5/l5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))