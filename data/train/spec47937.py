import numpy as np 

def function(x):

	j6 = x
	b1 = x
	paths = []
	try:
		if x > 8:
			x = x+2
			j6 = 6*j6
			paths.append(1)
		else:
			b1 = 8*b1
			paths.append(2)
		if x >= 5:
			j6 = j6/b1
			b1 = b1+5
			paths.append(3)
		else:
			x = 2+b1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))