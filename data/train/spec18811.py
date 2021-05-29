import numpy as np 

def function(x):

	l3 = 6
	n9 = x
	paths = []
	try:
		if n9 > 1:
			l3 = 1*2
			x = 3*l3
			paths.append(1)
		else:
			l3 = 2+8
			paths.append(2)
		if x >= 7:
			l3 = l3/l3
			l3 = l3+7
			paths.append(3)
		else:
			l3 = l3/6
			x = x*4
			l3 = l3-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))