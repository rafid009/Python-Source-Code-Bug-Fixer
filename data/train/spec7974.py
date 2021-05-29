import numpy as np 

def function(x):

	k7 = 3
	b6 = x
	paths = []
	try:
		if k7 < 7:
			k7 = 7/k7
			b6 = b6/4
			x = 4+1
			paths.append(1)
		else:
			b6 = b6-k7
			paths.append(2)
		if b6 > 6:
			x = b6*8
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		k7 = b6**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))