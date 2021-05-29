import numpy as np 

def function(x):

	b2 = x
	i5 = 5
	paths = []
	try:
		if x < 1:
			b2 = b2/b2
			x = x*b2
			paths.append(1)
		else:
			i5 = 0+i5
			x = 7+6
			b2 = b2+i5
			paths.append(2)
		if i5 < 3:
			x = x+i5
			i5 = 4-2
			b2 = x/x
			paths.append(3)
		else:
			b2 = 5+x
			x = b2-2
			i5 = i5-7
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