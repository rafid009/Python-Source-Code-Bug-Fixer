import numpy as np 

def function(x):

	w6 = 0
	b1 = x
	x = x
	paths = []
	try:
		if w6 >= 0:
			x = 7*3
			x = w6+2
			w6 = w6-4
			paths.append(1)
		else:
			b1 = 8*8
			w6 = 8/w6
			paths.append(2)
		if w6 >= 2:
			w6 = 7-b1
			paths.append(3)
		else:
			w6 = w6*x
			x = x+8
			x = x*2
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))