import numpy as np 

def function(x):

	d8 = 7
	n1 = x
	paths = []
	try:
		if x < 5:
			d8 = d8/9
			paths.append(1)
		else:
			n1 = 4/9
			x = x-1
			x = 7*9
			paths.append(2)
		if n1 >= 3:
			n1 = n1-4
			n1 = 8-7
			paths.append(3)
		else:
			x = d8*0
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))