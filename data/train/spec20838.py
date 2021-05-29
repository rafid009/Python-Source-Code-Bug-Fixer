import numpy as np 

def function(x):

	i7 = x
	b5 = x
	x = x
	paths = []
	try:
		if i7 < 7:
			b5 = 5*b5
			paths.append(1)
		else:
			b5 = 3/b5
			x = 5*b5
			x = 5*x
			paths.append(2)
		if x > 0:
			x = x*4
			paths.append(3)
		else:
			i7 = i7*3
			x = b5/i7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		b5 = i7**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))