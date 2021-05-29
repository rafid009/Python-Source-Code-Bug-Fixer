import numpy as np 

def function(x):

	n8 = 8
	f5 = 0
	paths = []
	try:
		if x < 4:
			f5 = f5+2
			x = n8+3
			n8 = 6/f5
			paths.append(1)
		else:
			f5 = n8-f5
			x = x-9
			paths.append(2)
		if x > 9:
			n8 = 6*x
			x = 4/x
			paths.append(3)
		else:
			n8 = 5/n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))