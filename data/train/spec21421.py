import numpy as np 

def function(x):

	e1 = 3
	n2 = 1
	paths = []
	try:
		if e1 <= 2:
			n2 = 9+7
			n2 = 8*e1
			paths.append(1)
		else:
			x = x/5
			n2 = 8+n2
			paths.append(2)
		if x >= 4:
			e1 = e1*8
			x = 3+x
			paths.append(3)
		else:
			e1 = 5*7
			e1 = e1/x
			n2 = x/n2
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))