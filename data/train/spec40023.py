import numpy as np 

def function(x):

	u5 = 4
	w6 = 4
	paths = []
	try:
		if x > 4:
			x = w6*x
			paths.append(1)
		else:
			u5 = w6*x
			w6 = w6+x
			x = u5/w6
			paths.append(2)
		if u5 >= 2:
			x = x*u5
			w6 = 3+8
			paths.append(3)
		else:
			u5 = 1-u5
			x = 2*5
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))