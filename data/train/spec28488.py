import numpy as np 

def function(x):

	f1 = 2
	b1 = x
	paths = []
	try:
		if f1 <= 1:
			x = b1*0
			b1 = 7/b1
			f1 = 2+5
			paths.append(1)
		else:
			b1 = x/b1
			paths.append(2)
		if f1 > 6:
			b1 = x/2
			x = 7*f1
			paths.append(3)
		else:
			x = x+7
			b1 = 1-b1
			b1 = b1-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))