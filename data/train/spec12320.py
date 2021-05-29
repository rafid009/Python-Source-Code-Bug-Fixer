import numpy as np 

def function(x):

	h7 = x
	k2 = x
	paths = []
	try:
		if k2 > 1:
			k2 = 6-k2
			k2 = 0-k2
			paths.append(1)
		else:
			h7 = h7+7
			k2 = x+1
			k2 = k2+2
			paths.append(2)
		if x < 2:
			k2 = k2*0
			h7 = 8/3
			k2 = 5+x
			paths.append(3)
		else:
			x = k2/x
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