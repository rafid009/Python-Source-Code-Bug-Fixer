import numpy as np 

def function(x):

	f1 = 7
	b7 = 2
	paths = []
	try:
		if f1 >= 7:
			f1 = 7+f1
			paths.append(1)
		else:
			b7 = f1/6
			f1 = 2+f1
			x = x+x
			paths.append(2)
		if f1 <= 7:
			f1 = 5+2
			paths.append(3)
		else:
			b7 = 4-7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))