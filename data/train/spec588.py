import numpy as np 

def function(x):

	w1 = 3
	i5 = x
	paths = []
	try:
		if x < 8:
			x = 5+x
			paths.append(1)
		else:
			i5 = 9*x
			w1 = w1+3
			w1 = 8*2
			paths.append(2)
		if i5 > 1:
			w1 = w1*2
			paths.append(3)
		else:
			w1 = w1+7
			x = 6-5
			w1 = 8*w1
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		w1 = i5**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))