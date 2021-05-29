import numpy as np 

def function(x):

	a7 = x
	b8 = 1
	paths = []
	try:
		if b8 >= 9:
			b8 = b8-a7
			b8 = b8+a7
			paths.append(1)
		else:
			x = x+3
			x = 1+6
			b8 = 4+8
			paths.append(2)
		if b8 <= 7:
			b8 = 1+b8
			paths.append(3)
		else:
			x = 0*6
			x = x*9
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		b8 = a7**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))