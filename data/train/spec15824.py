import numpy as np 

def function(x):

	w3 = 8
	u5 = 0
	paths = []
	try:
		if x <= 1:
			u5 = 3+u5
			u5 = x*7
			x = x+5
			paths.append(1)
		else:
			x = 9*w3
			w3 = x/4
			paths.append(2)
		if u5 > 0:
			u5 = u5/2
			x = x/6
			w3 = w3+7
			paths.append(3)
		else:
			w3 = w3-x
			x = 1/8
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