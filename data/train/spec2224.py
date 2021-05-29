import numpy as np 

def function(x):

	n1 = 2
	f6 = x
	paths = []
	try:
		if f6 > 5:
			n1 = n1*n1
			n1 = n1/n1
			x = f6/x
			paths.append(1)
		else:
			f6 = f6*x
			paths.append(2)
		if x <= 2:
			x = x*8
			f6 = f6/f6
			n1 = 0-8
			paths.append(3)
		else:
			n1 = n1+5
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