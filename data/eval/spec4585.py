import numpy as np 

def function(x):

	b8 = x
	o7 = x
	paths = []
	try:
		if b8 < 5:
			b8 = b8+5
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if b8 <= 7:
			x = x*3
			o7 = x+b8
			b8 = 5+b8
			paths.append(3)
		else:
			b8 = 2/8
			b8 = 1*x
			b8 = b8+8
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		b8 = o7**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))