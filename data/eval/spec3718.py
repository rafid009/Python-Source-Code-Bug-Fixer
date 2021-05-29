import numpy as np 

def function(x):

	u8 = 2
	b2 = 6
	paths = []
	try:
		if x < 7:
			u8 = u8+b2
			b2 = b2*b2
			x = 3*7
			paths.append(1)
		else:
			b2 = b2+5
			b2 = b2-b2
			b2 = b2+1
			paths.append(2)
		if x <= 9:
			u8 = 2+u8
			u8 = u8+4
			u8 = u8-x
			paths.append(3)
		else:
			b2 = b2-1
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		b2 = u8**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))