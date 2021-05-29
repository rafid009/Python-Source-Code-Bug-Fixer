import numpy as np 

def function(x):

	q0 = x
	h2 = 8
	paths = []
	try:
		if x < 4:
			h2 = 5-9
			paths.append(1)
		else:
			h2 = h2+h2
			paths.append(2)
		if x <= 6:
			x = x+q0
			x = x-1
			q0 = h2*1
			paths.append(3)
		else:
			x = x*3
			h2 = h2+x
			h2 = h2+q0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))