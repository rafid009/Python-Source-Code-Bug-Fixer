import numpy as np 

def function(x):

	k5 = 6
	w5 = x
	paths = []
	try:
		if k5 < 9:
			k5 = 3/k5
			x = w5+w5
			paths.append(1)
		else:
			k5 = x/w5
			paths.append(2)
		if x > 6:
			w5 = 5+1
			paths.append(3)
		else:
			x = x*x
			x = x*7
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		k5 = w5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))