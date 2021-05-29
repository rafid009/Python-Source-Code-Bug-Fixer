import numpy as np 

def function(x):

	k1 = 8
	x4 = x
	paths = []
	try:
		if k1 < 8:
			x = 3+2
			x4 = x4+8
			k1 = k1+0
			paths.append(1)
		else:
			x = 6*0
			x4 = x4+3
			k1 = k1+4
			paths.append(2)
		if x4 <= 9:
			x4 = 0+3
			x = k1*7
			paths.append(3)
		else:
			x4 = 2+3
			k1 = 3-k1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x4 = k1**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))