import numpy as np 

def function(x):

	h9 = 0
	u6 = 3
	paths = []
	try:
		if u6 <= 4:
			x = x/7
			u6 = u6*0
			u6 = 3*7
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if u6 <= 4:
			h9 = u6-h9
			x = 6+9
			paths.append(3)
		else:
			x = u6/x
			h9 = x+h9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))