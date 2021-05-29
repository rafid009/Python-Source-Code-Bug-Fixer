import numpy as np 

def function(x):

	b0 = 2
	j1 = x
	paths = []
	try:
		if x >= 8:
			j1 = 0+j1
			j1 = j1-0
			paths.append(1)
		else:
			j1 = j1-x
			paths.append(2)
		if x > 4:
			b0 = b0*6
			b0 = 1/7
			j1 = j1/1
			paths.append(3)
		else:
			b0 = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))