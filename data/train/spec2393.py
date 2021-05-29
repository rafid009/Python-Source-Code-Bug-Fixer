import numpy as np 

def function(x):

	k2 = x
	f8 = x
	paths = []
	try:
		if f8 > 4:
			k2 = 7+4
			paths.append(1)
		else:
			x = x-8
			x = x*2
			k2 = k2*k2
			paths.append(2)
		if f8 <= 4:
			k2 = f8*x
			paths.append(3)
		else:
			k2 = k2+7
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