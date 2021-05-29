import numpy as np 

def function(x):

	b7 = 2
	d7 = x
	paths = []
	try:
		if x > 9:
			b7 = d7/x
			b7 = 5*0
			paths.append(1)
		else:
			x = 6*4
			x = 6-x
			paths.append(2)
		if d7 > 6:
			d7 = d7+b7
			b7 = b7-6
			x = 6+x
			paths.append(3)
		else:
			d7 = 2-d7
			b7 = d7/3
			b7 = b7+8
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