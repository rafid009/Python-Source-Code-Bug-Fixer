import numpy as np 

def function(x):

	k9 = x
	l9 = x
	paths = []
	try:
		if x <= 6:
			x = k9+l9
			paths.append(1)
		else:
			l9 = l9-4
			x = x-9
			paths.append(2)
		if k9 < 3:
			x = x-7
			l9 = x/2
			paths.append(3)
		else:
			k9 = k9/l9
			k9 = 9+2
			k9 = 8-k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		l9 = k9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))