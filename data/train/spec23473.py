import numpy as np 

def function(x):

	n7 = x
	l3 = x
	paths = []
	try:
		if x >= 8:
			x = l3-5
			l3 = x*4
			n7 = 8-3
			paths.append(1)
		else:
			n7 = 5/n7
			l3 = 1*3
			paths.append(2)
		if l3 < 9:
			x = x+9
			x = 0-1
			paths.append(3)
		else:
			l3 = 1/3
			x = x-n7
			l3 = l3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))