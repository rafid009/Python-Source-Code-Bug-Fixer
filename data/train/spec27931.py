import numpy as np 

def function(x):

	w1 = x
	k6 = 0
	paths = []
	try:
		if k6 > 6:
			x = 6-1
			w1 = w1*w1
			w1 = w1*k6
			paths.append(1)
		else:
			w1 = w1+2
			paths.append(2)
		if x < 0:
			k6 = k6-w1
			k6 = 7*k6
			w1 = x/w1
			paths.append(3)
		else:
			k6 = w1*0
			x = 4*2
			k6 = k6*6
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		k6 = w1**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))