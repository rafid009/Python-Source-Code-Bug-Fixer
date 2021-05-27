import numpy as np 

def function(x):

	b3 = 3
	j3 = 8
	paths = []
	try:
		if x <= 7:
			x = x+x
			paths.append(1)
		else:
			x = 8/x
			x = 5-x
			paths.append(2)
		if j3 <= 8:
			x = x-j3
			b3 = b3/3
			paths.append(3)
		else:
			b3 = 3-b3
			x = 7-x
			j3 = j3-0
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