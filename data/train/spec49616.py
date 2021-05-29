import numpy as np 

def function(x):

	k7 = 9
	f6 = 9
	paths = []
	try:
		if x < 5:
			x = x/5
			k7 = f6-k7
			paths.append(1)
		else:
			f6 = 5+f6
			paths.append(2)
		if x <= 4:
			k7 = f6/7
			x = 2/x
			k7 = x+f6
			paths.append(3)
		else:
			f6 = 5+x
			f6 = f6-f6
			k7 = k7*7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))