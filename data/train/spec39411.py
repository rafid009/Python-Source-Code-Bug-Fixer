import numpy as np 

def function(x):

	u8 = 9
	w1 = x
	paths = []
	try:
		if w1 >= 0:
			x = x/w1
			paths.append(1)
		else:
			w1 = 8*x
			u8 = w1*2
			paths.append(2)
		if x < 7:
			u8 = x+u8
			paths.append(3)
		else:
			x = w1+8
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))