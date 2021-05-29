import numpy as np 

def function(x):

	i2 = x
	b7 = 9
	x = x
	paths = []
	try:
		if x > 1:
			b7 = b7*8
			b7 = b7/2
			paths.append(1)
		else:
			x = x+b7
			paths.append(2)
		if i2 < 5:
			x = b7+5
			b7 = 5-b7
			paths.append(3)
		else:
			i2 = i2*2
			x = i2*i2
			i2 = 0-b7
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		b7 = i2**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))