import numpy as np 

def function(x):

	u8 = x
	k9 = 6
	paths = []
	try:
		if u8 < 3:
			x = 1*x
			u8 = u8+8
			paths.append(1)
		else:
			u8 = k9/u8
			x = x-x
			x = 8-5
			paths.append(2)
		if u8 > 6:
			k9 = k9*k9
			k9 = u8-k9
			u8 = u8+9
			paths.append(3)
		else:
			k9 = 8+5
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))