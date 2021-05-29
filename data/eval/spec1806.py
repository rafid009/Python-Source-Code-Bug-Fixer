import numpy as np 

def function(x):

	k5 = x
	a4 = x
	paths = []
	try:
		if x > 3:
			x = 6*2
			paths.append(1)
		else:
			k5 = k5-8
			paths.append(2)
		if k5 <= 4:
			k5 = 2+1
			x = 6+x
			paths.append(3)
		else:
			k5 = k5+3
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		k5 = a4**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))