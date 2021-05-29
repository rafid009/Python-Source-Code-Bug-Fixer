import numpy as np 

def function(x):

	u2 = x
	b0 = 0
	paths = []
	try:
		if b0 <= 7:
			x = x-x
			u2 = u2-1
			x = u2+x
			paths.append(1)
		else:
			x = x*3
			x = 0+x
			u2 = x+0
			paths.append(2)
		if b0 <= 4:
			b0 = 1-b0
			paths.append(3)
		else:
			x = 6+u2
			b0 = b0+u2
			u2 = 7-u2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))