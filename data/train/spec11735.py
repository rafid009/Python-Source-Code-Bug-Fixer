import numpy as np 

def function(x):

	u8 = 0
	i3 = x
	x = x
	paths = []
	try:
		if i3 > 6:
			x = x/7
			u8 = u8*i3
			paths.append(1)
		else:
			i3 = 8-i3
			i3 = i3/5
			x = x-6
			paths.append(2)
		if x <= 9:
			i3 = 9-i3
			u8 = u8-x
			u8 = u8/x
			paths.append(3)
		else:
			x = x/9
			i3 = x+i3
			u8 = i3*5
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