import numpy as np 

def function(x):

	w7 = x
	b5 = 1
	paths = []
	try:
		if x < 9:
			b5 = b5-2
			b5 = 1*4
			paths.append(1)
		else:
			w7 = 1-5
			paths.append(2)
		if b5 > 2:
			x = w7*4
			w7 = 1/w7
			w7 = w7*0
			paths.append(3)
		else:
			x = x-7
			b5 = b5-b5
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		b5 = w7**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))