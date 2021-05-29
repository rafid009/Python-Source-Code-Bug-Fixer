import numpy as np 

def function(x):

	b3 = x
	j5 = x
	paths = []
	try:
		if j5 <= 5:
			x = 3*8
			x = x+b3
			paths.append(1)
		else:
			b3 = b3+b3
			paths.append(2)
		if x >= 6:
			x = 7/4
			x = 0+x
			paths.append(3)
		else:
			x = j5+2
			j5 = 8/j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))