import numpy as np 

def function(x):

	w3 = x
	f6 = 3
	x = 4
	paths = []
	try:
		if w3 > 0:
			f6 = w3+9
			f6 = 3+1
			f6 = x*x
			paths.append(1)
		else:
			f6 = x+2
			x = 6*9
			paths.append(2)
		if f6 >= 4:
			f6 = f6/f6
			f6 = 2+f6
			f6 = 9+f6
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		w3 = w3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))