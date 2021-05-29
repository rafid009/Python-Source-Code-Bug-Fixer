import numpy as np 

def function(x):

	u9 = x
	w6 = 4
	paths = []
	try:
		if w6 < 1:
			w6 = w6-u9
			u9 = 9*3
			paths.append(1)
		else:
			u9 = x+u9
			x = 4+x
			w6 = x+w6
			paths.append(2)
		if w6 > 6:
			x = 6+w6
			paths.append(3)
		else:
			w6 = 4+w6
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))