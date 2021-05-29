import numpy as np 

def function(x):

	b1 = 2
	j7 = x
	paths = []
	try:
		if j7 >= 7:
			b1 = b1+x
			x = x-x
			b1 = 9/j7
			paths.append(1)
		else:
			b1 = b1-x
			b1 = b1-x
			j7 = b1+1
			paths.append(2)
		if x > 3:
			j7 = 1/2
			b1 = 8*j7
			paths.append(3)
		else:
			b1 = b1*0
			b1 = 7-j7
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