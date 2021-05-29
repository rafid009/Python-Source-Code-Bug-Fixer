import numpy as np 

def function(x):

	j1 = x
	w1 = x
	paths = []
	try:
		if x <= 6:
			j1 = j1-w1
			paths.append(1)
		else:
			j1 = j1/7
			j1 = 2*j1
			j1 = 7+9
			paths.append(2)
		if w1 <= 6:
			x = 0+7
			paths.append(3)
		else:
			w1 = w1*8
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		j1 = w1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))