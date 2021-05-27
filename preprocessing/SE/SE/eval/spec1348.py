import numpy as np 

def function(x):

	r2 = 6
	k9 = x
	x = 8
	paths = []
	try:
		if r2 < 2:
			k9 = k9+k9
			x = x/r2
			paths.append(1)
		else:
			r2 = r2/7
			r2 = 3*r2
			x = x-4
			paths.append(2)
		if r2 > 0:
			r2 = 8+4
			x = x/6
			r2 = 0-x
			paths.append(3)
		else:
			r2 = r2+k9
			r2 = 4*r2
			x = 1+5
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