import numpy as np 

def function(x):

	i4 = x
	b5 = 9
	paths = []
	try:
		if x >= 8:
			x = x*2
			paths.append(1)
		else:
			x = 2+x
			b5 = 5+b5
			paths.append(2)
		if b5 >= 0:
			i4 = b5-i4
			b5 = 8-b5
			paths.append(3)
		else:
			x = x+2
			i4 = i4-i4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))