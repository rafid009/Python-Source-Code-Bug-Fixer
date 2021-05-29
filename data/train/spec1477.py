import numpy as np 

def function(x):

	k9 = x
	o6 = x
	paths = []
	try:
		if o6 > 9:
			o6 = k9*o6
			paths.append(1)
		else:
			x = 1-x
			k9 = 0+k9
			paths.append(2)
		if k9 <= 9:
			x = x+6
			k9 = k9*4
			x = 6*x
			paths.append(3)
		else:
			o6 = 8*o6
			x = x/8
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		o6 = k9**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))