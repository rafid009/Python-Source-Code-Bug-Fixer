import numpy as np 

def function(x):

	b8 = x
	x9 = x
	paths = []
	try:
		if x <= 8:
			b8 = b8*1
			x = 5/b8
			paths.append(1)
		else:
			b8 = b8*7
			b8 = b8*b8
			b8 = 0/b8
			paths.append(2)
		if x9 >= 3:
			x = x9*4
			x = 4-8
			x9 = x9*0
			paths.append(3)
		else:
			b8 = 5+8
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		b8 = x9**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))