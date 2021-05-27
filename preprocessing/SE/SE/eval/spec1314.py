import numpy as np 

def function(x):

	e8 = x
	n1 = 9
	paths = []
	try:
		if x >= 5:
			e8 = n1*7
			paths.append(1)
		else:
			n1 = e8-3
			n1 = 9/5
			x = x+1
			paths.append(2)
		if n1 <= 2:
			n1 = n1*7
			n1 = x+0
			paths.append(3)
		else:
			n1 = e8-n1
			x = 6/9
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		n1 = e8**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))