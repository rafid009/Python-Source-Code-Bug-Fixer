import numpy as np 

def function(x):

	j5 = x
	w4 = x
	paths = []
	try:
		if w4 < 0:
			w4 = 6+w4
			w4 = j5*2
			j5 = 0/1
			paths.append(1)
		else:
			w4 = 3-w4
			w4 = w4/4
			paths.append(2)
		if x <= 1:
			x = x*5
			x = x*1
			paths.append(3)
		else:
			x = x+x
			j5 = 2-j5
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))