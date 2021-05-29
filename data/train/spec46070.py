import numpy as np 

def function(x):

	w5 = 7
	n9 = 0
	x = x
	paths = []
	try:
		if w5 >= 3:
			w5 = x+8
			paths.append(1)
		else:
			n9 = n9/6
			paths.append(2)
		if n9 < 2:
			w5 = x*w5
			n9 = n9/x
			paths.append(3)
		else:
			n9 = 5*0
			x = x/4
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