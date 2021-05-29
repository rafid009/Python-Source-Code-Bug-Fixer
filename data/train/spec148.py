import numpy as np 

def function(x):

	d5 = 1
	k9 = x
	paths = []
	try:
		if k9 >= 3:
			x = 8-6
			d5 = x-d5
			paths.append(1)
		else:
			d5 = 9/1
			d5 = 7/d5
			paths.append(2)
		if d5 <= 0:
			d5 = d5-9
			x = x+4
			k9 = d5*k9
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))