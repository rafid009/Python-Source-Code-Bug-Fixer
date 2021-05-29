import numpy as np 

def function(x):

	w3 = 4
	f6 = x
	paths = []
	try:
		if w3 > 7:
			w3 = x-0
			f6 = 3/8
			w3 = w3-w3
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if f6 < 6:
			w3 = 6-x
			paths.append(3)
		else:
			f6 = f6-w3
			x = f6+1
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))