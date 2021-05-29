import numpy as np 

def function(x):

	b5 = x
	w3 = 1
	paths = []
	try:
		if x <= 4:
			x = x+9
			b5 = 1/x
			w3 = w3/w3
			paths.append(1)
		else:
			x = 6-x
			x = 6-4
			w3 = 8*8
			paths.append(2)
		if x > 6:
			x = x*b5
			x = 6+x
			paths.append(3)
		else:
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))