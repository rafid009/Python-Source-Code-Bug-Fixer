import numpy as np 

def function(x):

	i6 = 4
	w2 = 1
	paths = []
	try:
		if i6 >= 4:
			w2 = 5/w2
			w2 = w2*0
			paths.append(1)
		else:
			x = 7*i6
			i6 = 1*i6
			paths.append(2)
		if x < 1:
			i6 = i6*7
			paths.append(3)
		else:
			x = 8-x
			i6 = x-i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))