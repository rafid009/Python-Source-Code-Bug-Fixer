import numpy as np 

def function(x):

	w1 = x
	n8 = x
	paths = []
	try:
		if x > 5:
			n8 = 9-n8
			n8 = 5*x
			paths.append(1)
		else:
			x = n8+x
			paths.append(2)
		if x < 6:
			x = x-5
			w1 = n8+3
			paths.append(3)
		else:
			n8 = w1+9
			x = 2+w1
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))