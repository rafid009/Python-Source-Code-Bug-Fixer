import numpy as np 

def function(x):

	n7 = 9
	l3 = 6
	paths = []
	try:
		if x > 5:
			n7 = n7-3
			paths.append(1)
		else:
			l3 = x-3
			paths.append(2)
		if l3 <= 4:
			n7 = 9-n7
			n7 = n7-9
			paths.append(3)
		else:
			n7 = 0+3
			n7 = n7+1
			n7 = l3/4
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