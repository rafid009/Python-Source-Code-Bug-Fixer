import numpy as np 

def function(x):

	k9 = x
	x2 = 4
	x = x
	paths = []
	try:
		if x > 3:
			x = x*2
			x2 = 6-x2
			paths.append(1)
		else:
			x2 = x2*4
			x = 4+x
			paths.append(2)
		if x2 > 2:
			x2 = k9+x2
			x = x-x
			paths.append(3)
		else:
			x = x2/5
			x = 8-x
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))