import numpy as np 

def function(x):

	w6 = 0
	i0 = x
	x = x
	paths = []
	try:
		if w6 <= 0:
			w6 = w6*6
			x = w6*0
			x = x+3
			paths.append(1)
		else:
			w6 = 6*0
			x = x/8
			i0 = 3/i0
			paths.append(2)
		if i0 < 1:
			w6 = 9+x
			i0 = i0+8
			x = i0+i0
			paths.append(3)
		else:
			w6 = 7*w6
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))