import numpy as np 

def function(x):

	e9 = 5
	k9 = 0
	paths = []
	try:
		if x > 6:
			e9 = 4/9
			x = x+0
			paths.append(1)
		else:
			k9 = x-k9
			e9 = 1-1
			paths.append(2)
		if e9 < 5:
			e9 = 0-9
			paths.append(3)
		else:
			x = 4*3
			e9 = x*5
			k9 = x/k9
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))