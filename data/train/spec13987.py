import numpy as np 

def function(x):

	u8 = x
	k9 = 7
	paths = []
	try:
		if k9 < 0:
			k9 = 0-k9
			paths.append(1)
		else:
			k9 = 9*k9
			paths.append(2)
		if u8 < 2:
			x = x+x
			paths.append(3)
		else:
			u8 = k9/u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		k9 = u8**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))