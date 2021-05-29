import numpy as np 

def function(x):

	k7 = x
	w2 = x
	x = 9
	paths = []
	try:
		if w2 >= 9:
			x = x*3
			x = x/5
			k7 = k7/1
			paths.append(1)
		else:
			w2 = 5+k7
			k7 = k7/k7
			paths.append(2)
		if x <= 0:
			x = k7-2
			k7 = k7+7
			w2 = 1/4
			paths.append(3)
		else:
			k7 = k7/x
			w2 = 8*w2
			k7 = k7*9
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))