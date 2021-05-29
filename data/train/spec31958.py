import numpy as np 

def function(x):

	i6 = x
	w2 = x
	paths = []
	try:
		if w2 < 0:
			i6 = 0-i6
			i6 = i6-2
			x = i6/3
			paths.append(1)
		else:
			w2 = w2/1
			i6 = w2*i6
			paths.append(2)
		if x >= 3:
			i6 = i6+0
			x = 5/w2
			x = x+4
			paths.append(3)
		else:
			x = 7+w2
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