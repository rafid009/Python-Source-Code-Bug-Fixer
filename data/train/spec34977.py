import numpy as np 

def function(x):

	k6 = x
	w6 = x
	paths = []
	try:
		if x < 9:
			x = w6/3
			paths.append(1)
		else:
			k6 = k6/7
			x = 9*0
			paths.append(2)
		if w6 < 9:
			w6 = w6/4
			paths.append(3)
		else:
			w6 = w6*w6
			x = x+7
			w6 = w6+w6
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