import numpy as np 

def function(x):

	n2 = 8
	u8 = x
	paths = []
	try:
		if n2 <= 7:
			x = n2+0
			n2 = n2+6
			n2 = 5-n2
			paths.append(1)
		else:
			n2 = n2/9
			paths.append(2)
		if n2 >= 5:
			x = x/u8
			paths.append(3)
		else:
			u8 = u8*0
			u8 = 2/n2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u8 = x**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))