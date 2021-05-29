import numpy as np 

def function(x):

	b2 = x
	w6 = x
	paths = []
	try:
		if x <= 8:
			b2 = 2+b2
			paths.append(1)
		else:
			x = 4*2
			paths.append(2)
		if x <= 9:
			b2 = b2+9
			paths.append(3)
		else:
			x = 9-b2
			w6 = 2+w6
			b2 = b2+0
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