import numpy as np 

def function(x):

	b2 = x
	w5 = x
	x = x
	paths = []
	try:
		if b2 < 9:
			x = x+w5
			b2 = 8-0
			paths.append(1)
		else:
			w5 = 8/w5
			b2 = b2*5
			paths.append(2)
		if x > 9:
			x = 5*7
			paths.append(3)
		else:
			b2 = w5-b2
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		b2 = w5**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))