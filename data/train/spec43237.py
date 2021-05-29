import numpy as np 

def function(x):

	k1 = 2
	b8 = x
	x = 8
	paths = []
	try:
		if k1 > 3:
			k1 = b8*4
			b8 = x+b8
			b8 = b8+k1
			paths.append(1)
		else:
			x = b8*x
			x = x-0
			k1 = k1+5
			paths.append(2)
		if b8 > 7:
			b8 = k1*k1
			paths.append(3)
		else:
			k1 = k1/4
			k1 = 6-k1
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))