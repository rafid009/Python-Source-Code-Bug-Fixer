import numpy as np 

def function(x):

	i7 = x
	u8 = x
	paths = []
	try:
		if i7 >= 5:
			x = u8-9
			u8 = u8/x
			paths.append(1)
		else:
			u8 = u8*4
			i7 = x+x
			i7 = 4+i7
			paths.append(2)
		if x < 5:
			i7 = i7-i7
			paths.append(3)
		else:
			x = x/6
			i7 = i7-i7
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		u8 = u8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))