import numpy as np 

def function(x):

	w6 = 2
	b8 = x
	paths = []
	try:
		if b8 > 2:
			w6 = w6+b8
			b8 = x*6
			w6 = w6-6
			paths.append(1)
		else:
			b8 = 3+1
			paths.append(2)
		if b8 < 2:
			b8 = 6/8
			paths.append(3)
		else:
			x = x+w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))