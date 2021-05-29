import numpy as np 

def function(x):

	i9 = 5
	w1 = 2
	paths = []
	try:
		if i9 < 2:
			x = x*x
			paths.append(1)
		else:
			w1 = x+i9
			w1 = w1/9
			w1 = w1*0
			paths.append(2)
		if w1 >= 1:
			w1 = 0/w1
			x = 8+x
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))