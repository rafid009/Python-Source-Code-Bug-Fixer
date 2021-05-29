import numpy as np 

def function(x):

	k1 = x
	e4 = 9
	x = 9
	paths = []
	try:
		if k1 >= 7:
			k1 = k1*8
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if x > 5:
			x = 5+x
			x = e4+x
			e4 = x-e4
			paths.append(3)
		else:
			k1 = 7+k1
			x = x*k1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		k1 = k1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))