import numpy as np 

def function(x):

	f1 = x
	w5 = x
	paths = []
	try:
		if w5 > 1:
			x = 2-8
			x = 2+x
			x = 5*x
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if x <= 3:
			w5 = w5/2
			w5 = w5-4
			paths.append(3)
		else:
			w5 = w5*0
			f1 = 8+f1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))