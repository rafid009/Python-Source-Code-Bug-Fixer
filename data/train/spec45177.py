import numpy as np 

def function(x):

	k7 = x
	b3 = 9
	paths = []
	try:
		if k7 >= 5:
			k7 = 5/1
			paths.append(1)
		else:
			k7 = 1/6
			b3 = x+7
			x = 1+b3
			paths.append(2)
		if b3 > 1:
			k7 = 6+k7
			paths.append(3)
		else:
			k7 = 0*k7
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))