import numpy as np 

def function(x):

	k9 = 4
	u3 = x
	paths = []
	try:
		if x >= 9:
			k9 = k9-5
			u3 = 5-k9
			paths.append(1)
		else:
			k9 = 4/x
			paths.append(2)
		if u3 > 0:
			k9 = k9*7
			x = u3-x
			u3 = x-9
			paths.append(3)
		else:
			x = x*u3
			x = x*k9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))