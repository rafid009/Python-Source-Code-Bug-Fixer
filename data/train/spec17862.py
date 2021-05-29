import numpy as np 

def function(x):

	w2 = x
	z7 = 9
	x = 2
	paths = []
	try:
		if x > 7:
			w2 = x/2
			paths.append(1)
		else:
			z7 = w2/1
			w2 = w2+w2
			paths.append(2)
		if x < 7:
			z7 = z7-w2
			w2 = w2*1
			paths.append(3)
		else:
			w2 = w2-8
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))