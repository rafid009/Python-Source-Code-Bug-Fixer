import numpy as np 

def function(x):

	f8 = x
	b8 = x
	paths = []
	try:
		if b8 > 6:
			b8 = 7-b8
			paths.append(1)
		else:
			x = x*b8
			x = b8-x
			paths.append(2)
		if b8 <= 3:
			b8 = b8+7
			x = 3+x
			f8 = f8*4
			paths.append(3)
		else:
			x = 4*4
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		b8 = f8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))