import numpy as np 

def function(x):

	a7 = x
	b8 = x
	x = x
	paths = []
	try:
		if x <= 7:
			b8 = a7+x
			x = b8/9
			b8 = x+2
			paths.append(1)
		else:
			a7 = b8+5
			x = x+0
			a7 = a7-8
			paths.append(2)
		if b8 >= 9:
			b8 = a7/b8
			paths.append(3)
		else:
			x = a7/a7
			b8 = 8*2
			x = a7*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))