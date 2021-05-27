import numpy as np 

def function(x):

	w2 = 7
	j5 = x
	paths = []
	try:
		if x < 4:
			x = x*1
			paths.append(1)
		else:
			w2 = 0-5
			paths.append(2)
		if j5 >= 9:
			x = 2*x
			x = x+1
			w2 = 4*w2
			paths.append(3)
		else:
			j5 = j5*7
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		j5 = w2**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))