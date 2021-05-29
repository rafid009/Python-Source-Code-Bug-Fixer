import numpy as np 

def function(x):

	i3 = 4
	k9 = 4
	paths = []
	try:
		if x > 8:
			x = x*6
			k9 = k9/5
			k9 = 5-7
			paths.append(1)
		else:
			k9 = k9*3
			paths.append(2)
		if k9 <= 0:
			k9 = k9-3
			paths.append(3)
		else:
			i3 = i3+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))