import numpy as np 

def function(x):

	h2 = 6
	v1 = x
	paths = []
	try:
		if x > 6:
			v1 = 5-v1
			h2 = h2+7
			paths.append(1)
		else:
			v1 = v1-4
			x = 0/h2
			x = v1+2
			paths.append(2)
		if h2 > 7:
			x = h2+0
			h2 = x/h2
			x = 4/4
			paths.append(3)
		else:
			h2 = 6/h2
			x = 2/x
			h2 = 4/x
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))