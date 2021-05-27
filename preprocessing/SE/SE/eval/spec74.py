import numpy as np 

def function(x):

	j3 = x
	w1 = 6
	paths = []
	try:
		if j3 <= 0:
			j3 = 4+j3
			j3 = 8-j3
			j3 = j3-3
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if x < 7:
			w1 = j3-w1
			paths.append(3)
		else:
			w1 = w1*2
			w1 = 4-w1
			x = w1-3
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