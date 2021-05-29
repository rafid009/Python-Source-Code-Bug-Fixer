import numpy as np 

def function(x):

	w1 = x
	z6 = 7
	paths = []
	try:
		if z6 >= 7:
			w1 = w1/6
			paths.append(1)
		else:
			x = 0+x
			z6 = x*7
			paths.append(2)
		if z6 <= 2:
			w1 = w1*4
			paths.append(3)
		else:
			z6 = z6*2
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))