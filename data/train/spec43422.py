import numpy as np 

def function(x):

	k2 = 6
	j9 = x
	paths = []
	try:
		if j9 < 6:
			k2 = k2*9
			k2 = k2-1
			paths.append(1)
		else:
			j9 = j9-9
			j9 = j9+5
			paths.append(2)
		if k2 >= 8:
			j9 = x/7
			paths.append(3)
		else:
			x = 7/x
			j9 = 0*j9
			k2 = 2+k2
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))