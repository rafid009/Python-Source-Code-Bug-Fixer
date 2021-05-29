import numpy as np 

def function(x):

	b6 = x
	u4 = x
	paths = []
	try:
		if u4 > 5:
			x = x+5
			x = x/x
			b6 = b6/4
			paths.append(1)
		else:
			x = 4/u4
			u4 = b6/9
			u4 = u4-7
			paths.append(2)
		if b6 <= 4:
			u4 = 2-u4
			x = 2+x
			b6 = b6+8
			paths.append(3)
		else:
			u4 = u4/u4
			b6 = x-b6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))