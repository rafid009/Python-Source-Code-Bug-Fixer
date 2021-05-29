import numpy as np 

def function(x):

	w9 = 6
	a2 = 0
	x = 2
	paths = []
	try:
		if a2 > 6:
			w9 = x+3
			x = x-9
			a2 = a2*0
			paths.append(1)
		else:
			w9 = w9-1
			w9 = a2-w9
			paths.append(2)
		if a2 <= 8:
			a2 = a2*1
			paths.append(3)
		else:
			a2 = w9+a2
			a2 = w9*6
			w9 = 6+w9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		a2 = w9**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))