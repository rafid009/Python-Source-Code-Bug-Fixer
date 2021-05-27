import numpy as np 

def function(x):

	b4 = 4
	u2 = 7
	x = x
	paths = []
	try:
		if x >= 8:
			b4 = b4+3
			b4 = b4+u2
			paths.append(1)
		else:
			u2 = x*7
			x = x*3
			paths.append(2)
		if u2 < 1:
			b4 = b4*9
			paths.append(3)
		else:
			x = 7*0
			b4 = 4-b4
			b4 = 3-3
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