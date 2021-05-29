import numpy as np 

def function(x):

	u8 = 9
	k3 = x
	paths = []
	try:
		if u8 <= 1:
			k3 = k3+x
			x = x-0
			x = x*9
			paths.append(1)
		else:
			u8 = u8*9
			u8 = u8-x
			k3 = 8-u8
			paths.append(2)
		if u8 < 2:
			k3 = 2/4
			x = x+x
			u8 = u8+0
			paths.append(3)
		else:
			u8 = 4*u8
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		k3 = k3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))