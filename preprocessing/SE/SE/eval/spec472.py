import numpy as np 

def function(x):

	e9 = x
	n6 = x
	paths = []
	try:
		if e9 > 5:
			x = 0+e9
			e9 = 6/e9
			n6 = n6+5
			paths.append(1)
		else:
			n6 = n6/1
			x = x*8
			n6 = n6*4
			paths.append(2)
		if e9 <= 9:
			e9 = 2/e9
			x = e9*8
			paths.append(3)
		else:
			n6 = e9-n6
			x = x+7
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		n6 = e9**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))