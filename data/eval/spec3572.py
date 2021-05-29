import numpy as np 

def function(x):

	o4 = 9
	k9 = x
	paths = []
	try:
		if x <= 8:
			k9 = 1/k9
			o4 = 6/k9
			paths.append(1)
		else:
			k9 = 2+k9
			k9 = o4+6
			paths.append(2)
		if k9 <= 6:
			k9 = 5*o4
			paths.append(3)
		else:
			k9 = k9/o4
			o4 = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))