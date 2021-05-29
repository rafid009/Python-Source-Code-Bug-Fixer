import numpy as np 

def function(x):

	v2 = x
	l5 = 6
	paths = []
	try:
		if v2 > 5:
			v2 = 5-v2
			x = v2-2
			l5 = 5-x
			paths.append(1)
		else:
			l5 = 3*7
			v2 = 8/x
			paths.append(2)
		if v2 >= 1:
			l5 = 0/1
			paths.append(3)
		else:
			l5 = l5/8
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))