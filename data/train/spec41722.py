import numpy as np 

def function(x):

	k7 = 6
	v7 = x
	paths = []
	try:
		if k7 < 5:
			x = 4+1
			k7 = 1-v7
			v7 = 7*5
			paths.append(1)
		else:
			v7 = v7-2
			v7 = v7+3
			paths.append(2)
		if x < 9:
			v7 = k7-8
			x = k7/x
			paths.append(3)
		else:
			v7 = v7+v7
			k7 = v7*k7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		k7 = v7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))