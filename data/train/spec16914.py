import numpy as np 

def function(x):

	n1 = x
	i5 = 8
	paths = []
	try:
		if i5 <= 1:
			x = 7*x
			x = 1*2
			x = x/i5
			paths.append(1)
		else:
			x = x*3
			i5 = 2/i5
			paths.append(2)
		if n1 < 3:
			x = x+1
			i5 = x-n1
			n1 = x*2
			paths.append(3)
		else:
			i5 = 4*7
			i5 = i5/6
			n1 = 7*n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))