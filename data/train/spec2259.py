import numpy as np 

def function(x):

	w9 = x
	a2 = x
	paths = []
	try:
		if a2 > 3:
			x = x/4
			w9 = 8-w9
			paths.append(1)
		else:
			a2 = 1/7
			a2 = 2+4
			a2 = x+a2
			paths.append(2)
		if x >= 6:
			a2 = a2+x
			a2 = a2/6
			paths.append(3)
		else:
			a2 = 7-5
			w9 = w9*0
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))