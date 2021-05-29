import numpy as np 

def function(x):

	f8 = 2
	u8 = x
	paths = []
	try:
		if u8 > 6:
			f8 = 8-9
			paths.append(1)
		else:
			x = 2+x
			x = x*7
			paths.append(2)
		if f8 < 6:
			f8 = 8-5
			paths.append(3)
		else:
			x = 0-8
			x = 7*4
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		f8 = u8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))