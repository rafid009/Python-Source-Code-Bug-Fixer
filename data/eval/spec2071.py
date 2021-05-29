import numpy as np 

def function(x):

	k1 = 6
	f7 = x
	paths = []
	try:
		if x > 7:
			f7 = f7+9
			paths.append(1)
		else:
			f7 = 1+f7
			paths.append(2)
		if f7 < 3:
			f7 = 0+3
			k1 = k1-8
			x = x+8
			paths.append(3)
		else:
			k1 = 3-k1
			x = 3-8
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))