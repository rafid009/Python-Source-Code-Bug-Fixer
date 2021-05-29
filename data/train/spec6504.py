import numpy as np 

def function(x):

	k2 = 1
	b0 = x
	paths = []
	try:
		if b0 < 1:
			k2 = k2-b0
			x = 9-x
			paths.append(1)
		else:
			k2 = k2-7
			b0 = 4+1
			k2 = x/5
			paths.append(2)
		if k2 >= 7:
			x = 0+k2
			k2 = 5*k2
			k2 = k2*5
			paths.append(3)
		else:
			k2 = b0/7
			x = b0+k2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))