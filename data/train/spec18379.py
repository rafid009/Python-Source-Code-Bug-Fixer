import numpy as np 

def function(x):

	f5 = 6
	b7 = 4
	paths = []
	try:
		if f5 <= 5:
			x = x-b7
			paths.append(1)
		else:
			f5 = 4/f5
			f5 = 6/b7
			paths.append(2)
		if b7 > 7:
			f5 = 0/b7
			x = x+b7
			x = 5/x
			paths.append(3)
		else:
			b7 = b7*0
			b7 = 8-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))