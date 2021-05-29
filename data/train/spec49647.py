import numpy as np 

def function(x):

	j2 = 3
	w1 = x
	paths = []
	try:
		if x < 2:
			x = w1-3
			j2 = j2-0
			paths.append(1)
		else:
			j2 = j2-2
			j2 = 0*8
			w1 = w1+4
			paths.append(2)
		if j2 >= 5:
			j2 = 8-5
			j2 = 5-j2
			paths.append(3)
		else:
			x = x/7
			x = x*x
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