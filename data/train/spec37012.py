import numpy as np 

def function(x):

	w5 = 1
	n2 = 7
	paths = []
	try:
		if x < 1:
			x = x+2
			paths.append(1)
		else:
			w5 = n2+1
			paths.append(2)
		if n2 > 8:
			w5 = n2+w5
			x = 3/w5
			paths.append(3)
		else:
			w5 = w5-6
			n2 = n2-1
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		n2 = w5**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))