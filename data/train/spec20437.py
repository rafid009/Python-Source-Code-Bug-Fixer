import numpy as np 

def function(x):

	b1 = x
	i0 = 1
	paths = []
	try:
		if b1 <= 3:
			i0 = 3+b1
			b1 = b1*5
			paths.append(1)
		else:
			x = 8+2
			paths.append(2)
		if b1 < 5:
			i0 = 5*i0
			b1 = 1*b1
			paths.append(3)
		else:
			x = x+5
			x = x-7
			b1 = 2*1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		i0 = b1**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))