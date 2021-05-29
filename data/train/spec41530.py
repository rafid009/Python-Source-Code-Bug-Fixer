import numpy as np 

def function(x):

	d5 = x
	k9 = 0
	paths = []
	try:
		if k9 >= 1:
			d5 = d5+d5
			paths.append(1)
		else:
			d5 = x/x
			k9 = 7-9
			paths.append(2)
		if k9 <= 0:
			d5 = d5+2
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		d5 = k9**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))