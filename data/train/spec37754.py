import numpy as np 

def function(x):

	h4 = 6
	k9 = x
	paths = []
	try:
		if h4 >= 3:
			h4 = h4-x
			paths.append(1)
		else:
			k9 = 8-k9
			x = h4-x
			paths.append(2)
		if x < 2:
			x = h4+x
			x = 7+k9
			paths.append(3)
		else:
			x = x/h4
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