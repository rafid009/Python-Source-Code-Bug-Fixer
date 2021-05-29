import numpy as np 

def function(x):

	k7 = x
	r5 = x
	x = 7
	paths = []
	try:
		if r5 > 1:
			r5 = r5/8
			k7 = x+5
			paths.append(1)
		else:
			r5 = r5+6
			paths.append(2)
		if r5 >= 7:
			k7 = x+k7
			paths.append(3)
		else:
			k7 = k7*8
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))