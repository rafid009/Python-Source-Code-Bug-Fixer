import numpy as np 

def function(x):

	j0 = 8
	k9 = 7
	paths = []
	try:
		if x <= 4:
			j0 = j0*1
			x = x+x
			paths.append(1)
		else:
			x = x/k9
			paths.append(2)
		if j0 > 3:
			j0 = j0*8
			k9 = k9+9
			paths.append(3)
		else:
			j0 = j0/j0
			j0 = j0-1
			k9 = j0+9
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