import numpy as np 

def function(x):

	k9 = 8
	q8 = x
	paths = []
	try:
		if k9 >= 7:
			k9 = k9-k9
			x = 8+k9
			paths.append(1)
		else:
			q8 = 9+x
			q8 = k9-0
			q8 = q8-5
			paths.append(2)
		if q8 < 1:
			x = x+5
			x = x+2
			x = x+7
			paths.append(3)
		else:
			q8 = q8*9
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))