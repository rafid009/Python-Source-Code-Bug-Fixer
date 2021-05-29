import numpy as np 

def function(x):

	b8 = 7
	u4 = 3
	paths = []
	try:
		if b8 <= 0:
			x = x/x
			b8 = b8+u4
			paths.append(1)
		else:
			u4 = u4+u4
			u4 = b8+u4
			b8 = b8*6
			paths.append(2)
		if b8 <= 9:
			u4 = u4*0
			b8 = 5+b8
			x = x+0
			paths.append(3)
		else:
			b8 = 4+8
			x = x+2
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))