import numpy as np 

def function(x):

	w3 = 8
	f0 = 3
	paths = []
	try:
		if x > 6:
			w3 = w3-f0
			w3 = w3+w3
			w3 = 8/1
			paths.append(1)
		else:
			f0 = f0/x
			w3 = x*w3
			f0 = f0+3
			paths.append(2)
		if f0 > 7:
			f0 = 2+f0
			x = x+7
			paths.append(3)
		else:
			w3 = w3/f0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))