import numpy as np 

def function(x):

	d5 = x
	u8 = x
	paths = []
	try:
		if d5 >= 5:
			d5 = d5-d5
			x = x-6
			u8 = x*2
			paths.append(1)
		else:
			x = 6-x
			x = 8/u8
			x = x-4
			paths.append(2)
		if d5 <= 7:
			d5 = 2-d5
			paths.append(3)
		else:
			d5 = 5/3
			d5 = d5-1
			d5 = d5/7
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		u8 = d5**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))