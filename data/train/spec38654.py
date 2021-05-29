import numpy as np 

def function(x):

	i2 = x
	n2 = 8
	paths = []
	try:
		if x < 6:
			x = 8+x
			n2 = n2+2
			x = 9/x
			paths.append(1)
		else:
			i2 = 9+i2
			n2 = 1*n2
			paths.append(2)
		if x <= 5:
			i2 = i2*2
			paths.append(3)
		else:
			n2 = x/i2
			x = 6+x
			n2 = 0/i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		n2 = i2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))