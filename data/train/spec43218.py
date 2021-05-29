import numpy as np 

def function(x):

	b5 = x
	i2 = x
	paths = []
	try:
		if i2 >= 6:
			b5 = x*b5
			b5 = 7-b5
			b5 = 0*3
			paths.append(1)
		else:
			i2 = i2*x
			x = x+5
			b5 = b5+b5
			paths.append(2)
		if b5 <= 0:
			b5 = b5*1
			x = b5+x
			i2 = x+2
			paths.append(3)
		else:
			b5 = 5*b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))