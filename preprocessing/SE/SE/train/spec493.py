import numpy as np 

def function(x):

	i2 = 5
	b1 = 4
	paths = []
	try:
		if i2 >= 7:
			b1 = b1*5
			paths.append(1)
		else:
			i2 = b1+x
			x = 7-5
			paths.append(2)
		if b1 > 4:
			b1 = 3+6
			x = x*2
			i2 = 7/3
			paths.append(3)
		else:
			b1 = 2-b1
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))