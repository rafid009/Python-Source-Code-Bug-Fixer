import numpy as np 

def function(x):

	w6 = x
	u3 = 7
	paths = []
	try:
		if x <= 1:
			w6 = w6+8
			u3 = 6-7
			paths.append(1)
		else:
			w6 = w6+w6
			paths.append(2)
		if w6 > 5:
			u3 = 0+w6
			x = 2/x
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))