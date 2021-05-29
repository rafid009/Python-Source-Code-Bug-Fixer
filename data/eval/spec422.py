import numpy as np 

def function(x):

	l1 = 0
	o9 = x
	paths = []
	try:
		if l1 >= 5:
			x = 0/x
			paths.append(1)
		else:
			o9 = o9+l1
			o9 = 9+x
			x = x+9
			paths.append(2)
		if o9 <= 1:
			x = x+6
			l1 = 6*l1
			x = x*8
			paths.append(3)
		else:
			l1 = o9/9
			o9 = o9*7
			l1 = l1-o9
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