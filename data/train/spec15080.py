import numpy as np 

def function(x):

	f1 = 9
	b5 = 2
	paths = []
	try:
		if x <= 5:
			b5 = b5*4
			b5 = 7*b5
			f1 = f1*9
			paths.append(1)
		else:
			b5 = b5-1
			paths.append(2)
		if b5 < 4:
			x = 0/x
			x = x-3
			b5 = b5/f1
			paths.append(3)
		else:
			b5 = 4-b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))