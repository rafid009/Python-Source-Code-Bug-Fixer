import numpy as np 

def function(x):

	i6 = x
	u8 = 6
	paths = []
	try:
		if x >= 5:
			i6 = 8/i6
			i6 = 9+4
			paths.append(1)
		else:
			x = x/u8
			paths.append(2)
		if i6 <= 7:
			x = x+x
			i6 = 8/i6
			i6 = i6+x
			paths.append(3)
		else:
			u8 = i6-7
			u8 = 0/x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))