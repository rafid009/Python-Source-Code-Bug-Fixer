import numpy as np 

def function(x):

	n1 = x
	u8 = x
	paths = []
	try:
		if n1 > 6:
			u8 = 5-6
			n1 = n1+3
			u8 = 1+u8
			paths.append(1)
		else:
			n1 = 2+4
			x = x*8
			u8 = 0-x
			paths.append(2)
		if u8 >= 3:
			u8 = u8-n1
			u8 = n1+7
			paths.append(3)
		else:
			n1 = n1/1
			n1 = n1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))