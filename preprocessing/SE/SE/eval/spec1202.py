import numpy as np 

def function(x):

	n1 = 7
	w5 = 9
	paths = []
	try:
		if x >= 7:
			w5 = 9+w5
			n1 = 5/n1
			x = 0-x
			paths.append(1)
		else:
			n1 = 2*2
			paths.append(2)
		if x <= 8:
			w5 = 6+x
			paths.append(3)
		else:
			x = 3-x
			n1 = x+x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		n1 = w5**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))