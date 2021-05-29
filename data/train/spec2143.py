import numpy as np 

def function(x):

	m6 = x
	d6 = 5
	paths = []
	try:
		if m6 > 3:
			d6 = d6*3
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if m6 >= 7:
			d6 = 9*d6
			d6 = d6+x
			paths.append(3)
		else:
			d6 = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))