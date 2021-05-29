import numpy as np 

def function(x):

	k3 = 9
	b8 = x
	x = x
	paths = []
	try:
		if b8 < 8:
			k3 = k3+k3
			b8 = 5/b8
			paths.append(1)
		else:
			k3 = 2/4
			b8 = b8/1
			x = x-7
			paths.append(2)
		if k3 > 5:
			x = 9*1
			x = b8/b8
			paths.append(3)
		else:
			x = x+2
			b8 = 8/5
			k3 = k3-8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))