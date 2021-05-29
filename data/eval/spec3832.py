import numpy as np 

def function(x):

	o3 = x
	w2 = x
	paths = []
	try:
		if w2 <= 2:
			w2 = 4-7
			paths.append(1)
		else:
			o3 = 4/o3
			o3 = o3+1
			x = 7+x
			paths.append(2)
		if w2 < 9:
			x = x/w2
			x = o3-8
			paths.append(3)
		else:
			o3 = o3+0
			x = 9-9
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