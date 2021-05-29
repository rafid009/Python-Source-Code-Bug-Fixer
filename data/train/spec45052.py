import numpy as np 

def function(x):

	i7 = x
	w4 = x
	paths = []
	try:
		if i7 < 9:
			x = x/7
			w4 = i7+w4
			paths.append(1)
		else:
			x = i7*0
			x = w4+x
			paths.append(2)
		if i7 <= 6:
			w4 = 6-w4
			w4 = 7/x
			i7 = 1*1
			paths.append(3)
		else:
			x = w4-0
			w4 = i7+6
			i7 = i7+i7
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))