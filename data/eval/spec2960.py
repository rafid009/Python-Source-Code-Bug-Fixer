import numpy as np 

def function(x):

	d6 = x
	l5 = x
	paths = []
	try:
		if d6 < 8:
			x = x-x
			paths.append(1)
		else:
			d6 = d6+4
			x = 8+x
			paths.append(2)
		if d6 <= 3:
			x = d6*x
			paths.append(3)
		else:
			l5 = l5+d6
			x = x/3
			l5 = l5/1
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