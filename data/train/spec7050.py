import numpy as np 

def function(x):

	w8 = 0
	l1 = 4
	paths = []
	try:
		if l1 >= 9:
			x = x/6
			paths.append(1)
		else:
			w8 = x-4
			paths.append(2)
		if x <= 8:
			l1 = 2+2
			x = w8*8
			paths.append(3)
		else:
			x = 1+x
			w8 = w8*w8
			w8 = 1/w8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		l1 = w8**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))