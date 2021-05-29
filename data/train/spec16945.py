import numpy as np 

def function(x):

	d7 = x
	b2 = x
	paths = []
	try:
		if x <= 4:
			d7 = b2+x
			d7 = d7-b2
			x = d7+x
			paths.append(1)
		else:
			x = x+b2
			paths.append(2)
		if d7 >= 3:
			b2 = 3-b2
			b2 = 2-b2
			paths.append(3)
		else:
			d7 = d7-1
			x = x*x
			x = d7*7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))