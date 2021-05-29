import numpy as np 

def function(x):

	n7 = 6
	k7 = x
	paths = []
	try:
		if k7 >= 1:
			k7 = k7-5
			x = 5*x
			x = x/3
			paths.append(1)
		else:
			x = x-1
			n7 = n7*0
			k7 = 0*k7
			paths.append(2)
		if k7 <= 4:
			n7 = 2/7
			paths.append(3)
		else:
			n7 = n7+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))