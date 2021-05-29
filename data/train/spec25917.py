import numpy as np 

def function(x):

	b3 = 5
	j7 = 5
	paths = []
	try:
		if j7 <= 5:
			j7 = 4+7
			paths.append(1)
		else:
			j7 = j7+8
			paths.append(2)
		if j7 < 5:
			x = x/9
			x = 7+x
			b3 = b3+x
			paths.append(3)
		else:
			b3 = b3+0
			j7 = 4*b3
			b3 = 1/b3
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