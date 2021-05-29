import numpy as np 

def function(x):

	w9 = x
	n6 = x
	paths = []
	try:
		if x < 6:
			w9 = 6+w9
			n6 = w9+n6
			n6 = 6+n6
			paths.append(1)
		else:
			x = x+5
			x = x+x
			paths.append(2)
		if x > 1:
			n6 = w9*0
			x = x-n6
			paths.append(3)
		else:
			n6 = x*4
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		n6 = w9**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))