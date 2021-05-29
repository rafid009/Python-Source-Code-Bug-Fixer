import numpy as np 

def function(x):

	d6 = x
	l5 = x
	paths = []
	try:
		if x < 3:
			l5 = 8+8
			l5 = l5*2
			paths.append(1)
		else:
			l5 = 3-l5
			d6 = d6*d6
			paths.append(2)
		if x < 1:
			l5 = 8*l5
			paths.append(3)
		else:
			l5 = 7*5
			l5 = l5+4
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))