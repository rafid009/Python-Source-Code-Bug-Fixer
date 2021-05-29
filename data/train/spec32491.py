import numpy as np 

def function(x):

	w3 = 6
	w1 = 5
	paths = []
	try:
		if x <= 7:
			x = w1-x
			w1 = 3-w1
			paths.append(1)
		else:
			x = x/1
			w1 = w1*0
			w1 = w1/x
			paths.append(2)
		if w1 > 9:
			x = 7*1
			x = x*2
			paths.append(3)
		else:
			w1 = w1+w1
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