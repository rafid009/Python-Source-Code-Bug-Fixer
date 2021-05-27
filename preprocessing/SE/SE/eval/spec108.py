import numpy as np 

def function(x):

	w2 = x
	b5 = 1
	paths = []
	try:
		if x <= 0:
			b5 = b5-b5
			paths.append(1)
		else:
			x = x-x
			x = b5+b5
			x = x-w2
			paths.append(2)
		if x > 9:
			w2 = w2+9
			w2 = w2/b5
			w2 = 4/w2
			paths.append(3)
		else:
			x = x+6
			w2 = w2*8
			w2 = 5*w2
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