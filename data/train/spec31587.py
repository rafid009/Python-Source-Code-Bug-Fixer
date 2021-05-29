import numpy as np 

def function(x):

	w6 = x
	w4 = 8
	paths = []
	try:
		if x > 0:
			x = x+5
			w6 = w6+2
			x = w6-0
			paths.append(1)
		else:
			x = x+3
			x = 6*0
			x = 3/9
			paths.append(2)
		if w6 > 7:
			w4 = w4-1
			w6 = w6+x
			w4 = w4+1
			paths.append(3)
		else:
			x = x-x
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