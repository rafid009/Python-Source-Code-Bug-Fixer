import numpy as np 

def function(x):

	w0 = 7
	n1 = 0
	x = x
	paths = []
	try:
		if x <= 5:
			x = x+w0
			w0 = x*w0
			paths.append(1)
		else:
			x = 6/x
			n1 = x*0
			paths.append(2)
		if n1 > 1:
			x = x-6
			paths.append(3)
		else:
			n1 = x/4
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