import numpy as np 

def function(x):

	u5 = x
	w5 = x
	x = x
	paths = []
	try:
		if w5 < 7:
			x = 1-3
			x = x*7
			w5 = u5*7
			paths.append(1)
		else:
			w5 = 9/2
			x = x*x
			u5 = w5+1
			paths.append(2)
		if w5 >= 4:
			u5 = 1*0
			paths.append(3)
		else:
			x = w5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))