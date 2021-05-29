import numpy as np 

def function(x):

	k9 = 5
	y2 = 9
	paths = []
	try:
		if k9 > 0:
			k9 = k9-k9
			y2 = y2+y2
			y2 = k9*y2
			paths.append(1)
		else:
			y2 = 9+0
			y2 = y2/6
			y2 = y2+k9
			paths.append(2)
		if x <= 8:
			y2 = y2*7
			paths.append(3)
		else:
			k9 = 0*6
			y2 = y2*1
			y2 = y2-y2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))