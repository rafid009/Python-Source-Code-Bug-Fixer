import numpy as np 

def function(x):

	w1 = x
	j5 = x
	paths = []
	try:
		if w1 > 0:
			w1 = w1/x
			x = x+j5
			w1 = w1*3
			paths.append(1)
		else:
			w1 = 1/1
			w1 = j5*j5
			paths.append(2)
		if x >= 7:
			x = 7*8
			paths.append(3)
		else:
			w1 = j5/5
			j5 = 6*1
			j5 = j5/7
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))