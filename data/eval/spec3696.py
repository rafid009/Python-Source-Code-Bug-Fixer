import numpy as np 

def function(x):

	k9 = 7
	u7 = 2
	paths = []
	try:
		if u7 < 5:
			u7 = 1/u7
			paths.append(1)
		else:
			k9 = k9/x
			u7 = 9*u7
			k9 = 8-k9
			paths.append(2)
		if x < 7:
			k9 = u7*8
			x = u7*u7
			k9 = x-4
			paths.append(3)
		else:
			k9 = x+8
			u7 = u7-k9
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