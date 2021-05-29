import numpy as np 

def function(x):

	b0 = x
	f1 = x
	paths = []
	try:
		if x <= 1:
			x = x/x
			b0 = b0/b0
			x = 7*7
			paths.append(1)
		else:
			b0 = f1+b0
			paths.append(2)
		if b0 >= 3:
			x = x-2
			f1 = 7-f1
			b0 = 5-b0
			paths.append(3)
		else:
			x = 5-x
			b0 = b0*b0
			b0 = 8-b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		f1 = b0**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))