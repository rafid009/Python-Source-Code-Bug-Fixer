import numpy as np 

def function(x):

	d5 = x
	l9 = 8
	paths = []
	try:
		if x > 4:
			d5 = 0/d5
			x = x+9
			paths.append(1)
		else:
			l9 = 7/l9
			d5 = d5-0
			paths.append(2)
		if l9 <= 7:
			l9 = 8-7
			d5 = 6/6
			paths.append(3)
		else:
			d5 = 9*4
			l9 = l9/1
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