import numpy as np 

def function(x):

	w6 = x
	b7 = 5
	paths = []
	try:
		if b7 <= 8:
			b7 = b7*b7
			x = x-8
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if b7 <= 6:
			w6 = w6-9
			w6 = w6/b7
			w6 = w6/4
			paths.append(3)
		else:
			x = 5/w6
			w6 = w6*2
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		b7 = w6**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))