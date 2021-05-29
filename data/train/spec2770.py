import numpy as np 

def function(x):

	w9 = 8
	f2 = x
	paths = []
	try:
		if w9 <= 3:
			x = x+7
			w9 = w9*2
			x = f2*x
			paths.append(1)
		else:
			w9 = w9+w9
			f2 = 2/f2
			paths.append(2)
		if w9 > 2:
			w9 = x+x
			f2 = 7+f2
			paths.append(3)
		else:
			f2 = f2*1
			x = x/2
			w9 = 0+w9
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