import numpy as np 

def function(x):

	w3 = x
	u9 = 5
	paths = []
	try:
		if w3 <= 2:
			u9 = 2/u9
			w3 = 9+w3
			paths.append(1)
		else:
			u9 = u9+0
			w3 = 7-w3
			paths.append(2)
		if x < 9:
			u9 = u9/5
			x = x+w3
			u9 = x+8
			paths.append(3)
		else:
			x = 2-u9
			x = x+7
			u9 = u9/6
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